#!/usr/bin/env python3.7

# Author: Roujia Li
# email: Roujia.li@mail.utoronto.ca

import sys
import os
import pandas as pd
import gzip
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests
import argparse
import time
import subprocess
from TileSeqMut import help_functions
from Bio.Data.IUPACData import protein_letters_1to3
sys.path.append('..')

def get_clinvar(data_path):
    """
    If no clinvar dataset present, download from db
    """
    clinvar_tsv = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz"
    cmd = f"wget -N -P {data_path} {clinvar_tsv}"
    os.system(cmd)
    return os.path.join(data_path, "variant_summary.txt.gz")


def parse_clinvar_gnomad(clinvar_master_file, gene_symbol, mave_file, output_dir, range, varity=pd.DataFrame({})):
    """
    From clinvar master file, get variants for gene_id
    save gene_id and it's variants to a separate file
    """
    main_log = help_functions.logginginit("info", os.path.join(output_dir, "prc_main.log"))
    main_logger = main_log.getLogger("prc.log")
    main_logger.info(f"Start analyzing gene {gene_symbol}, using scores {mave_file}")
    clinvar_gene = []
    with gzip.open(clinvar_master_file, 'r') as clinvar:
        for line in clinvar:
            l = line.decode("utf-8").strip().split("\t")
            if l[0].startswith("#"):
                clinvar_gene.append(l)
            if l[4] == gene_symbol:
                clinvar_gene.append(l)
    clinvar_gene_df = pd.DataFrame(clinvar_gene)
    clinvar_gene_df, clinvar_gene_df.columns = clinvar_gene_df[1:], clinvar_gene_df.iloc[0]

    clinvar_gene_df['hgvsp'] = clinvar_gene_df['Name'].str.extract('(p\.[A-Za-z0-9=]*)', expand=True)
    merged_mave_df = merge_mave(clinvar_gene_df, mave_file)
    main_logger.info("Obtained clinvar data...")
    # get gnomad missense variants
    gnomad_df = get_gnomad(gene_symbol)
    # filter with 0.0001
    gnomad_common = gnomad_df[gnomad_df["genome_af"] > 0.0001][["hgvs", "genome_af"]]
    main_logger.info("Obtained gnomAD data...")
    # filter by assembly (assume we are using grch38)
    filter_df = merged_mave_df[merged_mave_df["Assembly"] == "GRCh38"]
    # remove mutaions with no hgvs
    filter_df = filter_df[(filter_df["hgvsp"].notnull()) & (filter_df["Name"].str.contains("p\.\?") == False)
                            & (filter_df["hgvsp"].str.contains("=") == False)]

    # simplify clinvar annotation
    filter_df["clinvar_anno"] = "Uncertain/Conflicting"
    filter_df.loc[filter_df["ClinicalSignificance"].str.contains("Pathogenic", case=False), "clinvar_anno"] = \
        "Pathogenic/Likely pathogenic"
    filter_df.loc[filter_df["ClinicalSignificance"].str.contains("Benign", case=False), "clinvar_anno"] = \
        "Benign/Likely benign"
    # save raw data to file
    gene_clinvar_file = os.path.join(output_dir, f"{gene_symbol}_clinvar.csv")
    filter_df.to_csv(gene_clinvar_file)
    # filter variants by range (if provided)
    # range is a tuple of two int
    # extract protein number from hgvsp
    filter_df["pro_pos"] = filter_df["hgvsp"].str.extract('(\d+)').astype(int)
    # if only want variants in a specific range
    if len(range) != 0:
        filter_df = filter_df[(filter_df["pro_pos"] >= range[0]) & (filter_df["pro_pos"] <= range[1])]

    # merge with gnomAD
    filter_with_gnomad = pd.merge(filter_df, gnomad_common, how="left", left_on="hgvsp", right_on="hgvs")
    # filter_with_gnomad = filter_with_gnomad[["hgvsp", "score", ""]]
    # merge with varity if provided
    if not varity.empty:
        filter_with_gnomad = pd.merge(filter_with_gnomad, varity, how="left", on="hgvsp")
    # make plots for clinvar data
    plot_clinvar_annotation(filter_with_gnomad, gene_symbol, range, output_dir)

    # simplify clinvar annotation for PRC curve
    filter_with_gnomad["pathogenic"] = np.nan
    filter_with_gnomad.loc[filter_with_gnomad["ClinicalSignificance"].str.contains("Pathogenic", case=False), "pathogenic"] = True
    filter_with_gnomad.loc[filter_with_gnomad["genome_af"].notnull(), "pathogenic"] = False
    filter_with_gnomad.loc[filter_with_gnomad["ClinicalSignificance"].str.contains("Benign", case=False),"pathogenic"] = False

    # FLIP DMS score
    filter_with_gnomad["MAVE"] = - filter_with_gnomad["score"]
    if not varity.empty:
        prc_df = filter_with_gnomad[["pathogenic", "MAVE", "VARITY_ER"]].dropna()
    else:
        prc_df = filter_with_gnomad[["pathogenic", "MAVE"]].dropna()

    prc_file = os.path.join(output_dir, "prc_file.csv")
    prc_df.to_csv(prc_file, index=False)
    n_p = prc_df[prc_df["pathogenic"]==True].shape[0]
    n_b = prc_df[prc_df["pathogenic"]==False].shape[0]
    plot_title = f"{gene_symbol} - {os.path.basename(mave_file).split('.')[0]} (P/LP: {n_p}, B/LB/gnomAD common: {n_b})"
    output_file = os.path.join(output_dir, f"{os.path.basename(mave_file).split('.')[0]}_PRC.pdf")
    call_prc(prc_file, plot_title, output_file)


def merge_mave(clinvar_df, mave_file):
    """
    Merge clinvar data with MAVE data (user input)
    """
    mave_df = pd.read_csv(mave_file, skiprows=15)
    merge_df = pd.merge(clinvar_df, mave_df, how="left", left_on="hgvsp", right_on="hgvs_pro")
    return merge_df


def get_gnomad(gene_ID):
    """
    From gnomad database grep variants for input gene

    gene: ENSG id of the gene
    return: variants with allele frequencies
    """
    # q = """
    #   {
    #     gene(gene_id: "%s", reference_genome:GRCh38){
    #     variants(dataset: gnomad_r3) {
    #     consequence
    #     isCanon: consequence_in_canonical_transcript
    #     pos
    #     variantId
    #     hgvs
    #     hgvsc
    #     hgvsp
    #     genome {
    #     af
    #     }
    #     }
    #     }
    #     }
    #     """ % self._gene_id

    # use gene_symbol
    q = """
            {
                gene(reference_genome: GRCh38, gene_symbol: "%s"){
                variants(dataset: gnomad_r3) {
                consequence
                pos
                variantId
                hgvs
                ref
                alt
                hgvsc
                hgvsp
                genome {
                af
                }
                exome {
                af
                }
                }
                }

            }""" % gene_ID
    # send request
    r = requests.post("https://gnomad.broadinstitute.org/api", json={'query': q})
    while r.status_code != 200:
        print(r.status_code)
        time.sleep(60)
        r = requests.post("https://gnomad.broadinstitute.org/api", json={'query': q})

    variants = r.json()
    if variants["data"]["gene"] is None:
        raise ValueError("ERROR: NO DATA FROM GNOMAD")
        # return pd.DataFrame(
        #     columns=['consequence', 'pos', 'variantId', 'hgvs', 'ref', 'alt', 'hgvsc', 'hgvsp', 'genome', 'exome',
        #              'cds_pos'])

    variants_dict = variants["data"]["gene"]["variants"]
    # convert response to dataframe
    df = pd.DataFrame.from_dict(variants_dict)
    if df.empty:
        raise ValueError("ERROR: NO DATA FROM GNOMAD")
        # return pd.DataFrame(
        #     columns=['consequence', 'pos', 'variantId', 'hgvs', 'ref', 'alt', 'hgvsc', 'hgvsp', 'genome', 'exome',
        #              'cds_pos'])

    coding_variants = df[df.hgvsp.notnull()]
    # extract cds position using regex
    coding_variants["cds_pos"] = coding_variants['hgvsc'].str.extract('(\d+)', expand=True)
    # remove nonsense and syn variants
    coding_variants = coding_variants[coding_variants["consequence"] == "missense_variant"]
    # change genome af format
    # coding_variants["genome"] = coding_variants["genome"].astype(dict)
    coding_variants["genome_af"] = pd.json_normalize(coding_variants["genome"])

    return coding_variants


def get_varity(varity_file):
    """
    Parse input varity file
    The raw file downloaded from VARITY website
    """
    varity_df = pd.read_csv(varity_file)
    varity_df = varity_df[["aa_pos", "aa_ref", "aa_alt", "VARITY_R", "VARITY_ER"]]
    # remove nonsense
    varity_df = varity_df[varity_df["aa_alt"].str.contains("\*") == False]
    # drop na
    varity_df =varity_df.dropna()
    # make hgvspro
    varity_df["aa_ref3"] = varity_df['aa_ref'].apply(lambda x: protein_letters_1to3[x.strip()] if type(x) == str
    else x)
    varity_df["aa_alt3"] = varity_df['aa_alt'].apply(lambda x: protein_letters_1to3[x.strip()] if type(x) == str
    else x)
    varity_df["hgvsp"] = "p." + varity_df["aa_ref3"] + varity_df["aa_pos"].astype(int).astype(str) + varity_df[
        "aa_alt3"]

    return varity_df[["hgvsp", "VARITY_R", "VARITY_ER"]]


def call_prc(prc_file, plot_title, output_file):
    """
    Use yogiroc_embeded.R to make prc plots
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output = subprocess.run([f"Rscript", os.path.join(current_dir, 'yogiroc_embeded.R'), prc_file, plot_title,
                             output_file], capture_output=True, text=True)



###### make plots #######
def plot_clinvar_annotation(df, gene_name, range, output):
    """
    For input df, plt clinvar_annotation
    """

    annotation = df["clinvar_anno"].value_counts().to_frame().reset_index()
    annotation.columns = ["Type", "Count"]
    if len(range) == 0:
        t = f"{gene_name} clinvar variants"
    else:
        t = f"{gene_name} clinvar variants {range[0], range[1]}"
    sns.barplot(x="Count", y="Type", data=annotation)
    plt.title(t)
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(output, f"{gene_name}_clinvar_annotation_missense.pdf"))
    plt.close()


if __name__ == '__main__':
    # for testing
    parser = argparse.ArgumentParser(description='Make PRC curve using DMS scores')
    # user input arguments
    # required!
    parser.add_argument("-s", "--scores", help="Input score file to make prc curve. score file ends with "
                                               "_simple_aa.csv", type=str, required=True)
    parser.add_argument("-g", "--gene", help="Gene symbol", type=str, required=True)

    # optional
    parser.add_argument("-c", "--clinvar", help="Path to Clinvar data, if not provided, the clinvar database will be "
                                                "download to output dir, this might take sometime.")
    parser.add_argument("-o", "--output", help="Output folder, if not specified, output plots will be saved with "
                                               "score file", type=str)
    parser.add_argument("-r", "--range", help="Two integers to indicate the start/end of the targeted region. If "
                                              "specified, only variants in this range will be included. e.g -r 0 180 "
                                              "means variants in the range of (0, 180] will be included for PRC curve",
                        nargs=2, type=int)
    parser.add_argument("-v", "--varity", help="File contains hgvsp and VARITY scores (VARITY_R and VARITY_ER) must "
                                               "be in columns.", type=str)
    args = parser.parse_args()

    # process input range
    aa_range = tuple(args.range)
    # define output directory
    if args.output is None:
        output_dir = os.path.dirname(args.scores)
    else:
        output_dir = args.output

    if args.clinvar is None:
        clinvar_data = get_clinvar(output_dir)
    else:
        clinvar_data = args.clinvar

    if args.varity is not None:
        varity_data = get_varity(args.varity)
        parse_clinvar_gnomad(clinvar_data, args.gene, args.scores, output_dir, aa_range, varity=varity_data)
    else:
        parse_clinvar_gnomad(clinvar_data, args.gene, args.scores, output_dir, aa_range)