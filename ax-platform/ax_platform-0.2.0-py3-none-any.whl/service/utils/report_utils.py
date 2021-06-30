#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from collections import defaultdict
from logging import Logger
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from ax.core.experiment import Experiment
from ax.core.metric import Metric
from ax.core.multi_type_experiment import MultiTypeExperiment
from ax.core.objective import MultiObjective, ScalarizedObjective
from ax.core.search_space import SearchSpace
from ax.core.trial import BaseTrial, Trial
from ax.modelbridge import ModelBridge
from ax.modelbridge.generation_strategy import GenerationStrategy
from ax.plot.contour import interact_contour_plotly
from ax.plot.slice import plot_slice_plotly
from ax.plot.trace import optimization_trace_single_method_plotly
from ax.utils.common.logger import get_logger
from ax.utils.common.typeutils import checked_cast, not_none


logger: Logger = get_logger(__name__)


def _get_objective_trace_plot(
    experiment: Experiment,
    metric_name: str,
    model_transitions: List[int],
    optimization_direction: Optional[str] = None,
    # pyre-ignore[11]: Annotation `go.Figure` is not defined as a type.
) -> Optional[go.Figure]:
    best_objectives = np.array([experiment.fetch_data().df["mean"]])
    return optimization_trace_single_method_plotly(
        y=best_objectives,
        title="Best objective found vs. # of iterations",
        ylabel=metric_name,
        model_transitions=model_transitions,
        optimization_direction=optimization_direction,
        plot_trial_points=True,
    )


def _get_objective_v_param_plot(
    search_space: SearchSpace,
    model: ModelBridge,
    metric_name: str,
    trials: Dict[int, BaseTrial],
) -> Optional[go.Figure]:
    range_params = list(search_space.range_parameters.keys())
    if len(range_params) == 1:
        # individual parameter slice plot
        output_slice_plot = plot_slice_plotly(
            model=not_none(model),
            param_name=range_params[0],
            metric_name=metric_name,
            generator_runs_dict={
                str(t.index): not_none(checked_cast(Trial, t).generator_run)
                for t in trials.values()
            },
        )
        return output_slice_plot
    if len(range_params) > 1:
        # contour plot
        output_contour_plot = interact_contour_plotly(
            model=not_none(model),
            metric_name=metric_name,
        )
        return output_contour_plot
    # if search space contains no range params
    logger.warning(
        "_get_objective_v_param_plot requires a search space with at least one "
        "RangeParameter. Returning None."
    )
    return None


def _get_suffix(input_str: str, delim: str = ".", n_chunks: int = 1) -> str:
    return delim.join(input_str.split(delim)[-n_chunks:])


def _get_shortest_unique_suffix_dict(
    input_str_list: List[str], delim: str = "."
) -> Dict[str, str]:
    """Maps a list of strings to their shortest unique suffixes

    Maps all original strings to the smallest number of chunks, as specified by
    delim, that are not a suffix of any other original string. If the original
    string was a suffix of another string, map it to its unaltered self.

    Args:
        input_str_list: a list of strings to create the suffix mapping for
        delim: the delimiter used to split up the strings into meaningful chunks

    Returns:
        dict: A dict with the original strings as keys and their abbreviations as
            values
    """

    # all input strings must be unique
    assert len(input_str_list) == len(set(input_str_list))
    if delim == "":
        raise ValueError("delim must be a non-empty string.")
    suffix_dict = defaultdict(list)
    # initialize suffix_dict with last chunk
    for istr in input_str_list:
        suffix_dict[_get_suffix(istr, delim=delim, n_chunks=1)].append(istr)
    max_chunks = max(len(istr.split(delim)) for istr in input_str_list)
    if max_chunks == 1:
        return {istr: istr for istr in input_str_list}
    # the upper range of this loop is `max_chunks + 2` because:
    #     - `i` needs to take the value of `max_chunks`, hence one +1
    #     - the contents of the loop are run one more time to check if `all_unique`,
    #           hence the other +1
    for i in range(2, max_chunks + 2):
        new_dict = defaultdict(list)
        all_unique = True
        for suffix, suffix_str_list in suffix_dict.items():
            if len(suffix_str_list) > 1:
                all_unique = False
                for istr in suffix_str_list:
                    new_dict[_get_suffix(istr, delim=delim, n_chunks=i)].append(istr)
            else:
                new_dict[suffix] = suffix_str_list
        if all_unique:
            if len(set(input_str_list)) != len(suffix_dict.keys()):
                break
            return {
                suffix_str_list[0]: suffix
                for suffix, suffix_str_list in suffix_dict.items()
            }
        suffix_dict = new_dict
    # If this function has not yet exited, some input strings still share a suffix.
    # This is not expected, but in this case, the function will return the identity
    # mapping, i.e., a dict with the original strings as both keys and values.
    logger.warning(
        "Something went wrong. Returning dictionary with original strings as keys and "
        "values."
    )
    return {istr: istr for istr in input_str_list}


def get_standard_plots(
    experiment: Experiment, generation_strategy: GenerationStrategy
) -> List[go.Figure]:
    """Extract standard plots for single-objective optimization.

    Extracts a list of plots from an Experiment and GenerationStrategy of general
    interest to an Ax user. Currently not supported are
    - TODO: multi-objective optimization
    - TODO: ChoiceParameter plots

    Args:
        - experiment: the Experiment from which to obtain standard plots.
        - generation_strategy: the GenerationStrategy used to suggest trial parameters
          in experiment

    Returns:
        - a plot of objective value vs. trial index, to show experiment progression
        - a plot of objective value vs. range parameter values, only included if the
          model associated with generation_strategy can create predictions. This
          consists of:

            - a plot_slice plot if the search space contains one range parameter
            - an interact_contour plot if the search space contains multiple
              range parameters

    """

    objective = not_none(experiment.optimization_config).objective
    if isinstance(objective, MultiObjective):
        logger.warning(
            "get_standard_plots does not currently support MultiObjective "
            "optimization experiments. Returning an empty list."
        )
        return []
    if isinstance(objective, ScalarizedObjective):
        logger.warning(
            "get_standard_plots does not currently support ScalarizedObjective "
            "optimization experiments. Returning an empty list."
        )
        return []

    if experiment.fetch_data().df.empty:
        logger.info(f"Experiment {experiment} does not yet have data, nothing to plot.")
        return []

    output_plot_list = []
    output_plot_list.append(
        _get_objective_trace_plot(
            experiment=experiment,
            metric_name=not_none(experiment.optimization_config).objective.metric.name,
            # TODO: Adjust `model_transitions` to case where custom trials are present
            # and generation strategy does not start right away.
            model_transitions=generation_strategy.model_transitions,
            optimization_direction=(
                "minimize"
                if not_none(experiment.optimization_config).objective.minimize
                else "maximize"
            ),
        )
    )

    # Objective vs. parameter plot requires a `Model`, so add it only if model
    # is alrady available. In cases where initially custom trials are attached,
    # model might not yet be set on the generation strategy.
    if generation_strategy.model:
        try:
            output_plot_list.append(
                _get_objective_v_param_plot(
                    search_space=experiment.search_space,
                    model=not_none(generation_strategy.model),
                    metric_name=not_none(
                        experiment.optimization_config
                    ).objective.metric.name,
                    trials=experiment.trials,
                )
            )
        except NotImplementedError:
            # Model does not implement `predict` method.
            pass

    return [plot for plot in output_plot_list if plot is not None]


def exp_to_df(
    exp: Experiment,
    metrics: Optional[List[Metric]] = None,
    run_metadata_fields: Optional[List[str]] = None,
    **kwargs: Any,
) -> pd.DataFrame:
    """Transforms an experiment to a DataFrame. Only supports Experiment and
    SimpleExperiment.

    Transforms an Experiment into a dataframe with rows keyed by trial_index
    and arm_name, metrics pivoted into one row.

    Args:
        exp: An Experiment that may have pending trials.
        metrics: Override list of metrics to return. Return all metrics if None.
        run_metadata_fields: fields to extract from trial.run_metadata for trial
            in experiment.trials. If there are multiple arms per trial, these
            fields will be replicated across the arms of a trial.
        **kwargs: Custom named arguments, useful for passing complex
            objects from call-site to the `fetch_data` callback.

    Returns:
        DataFrame: A dataframe of inputs, metadata and metrics by trial and arm. If
        no trials are available, returns an empty dataframe. If no metric ouputs are
        available, returns a dataframe of inputs and metadata.
    """

    def prep_return(
        df: pd.DataFrame, drop_col: str, sort_by: List[str]
    ) -> pd.DataFrame:
        return not_none(not_none(df.drop(drop_col, axis=1)).sort_values(sort_by))

    # Accept Experiment and SimpleExperiment
    if isinstance(exp, MultiTypeExperiment):
        raise ValueError("Cannot transform MultiTypeExperiments to DataFrames.")

    key_components = ["trial_index", "arm_name"]

    # Get each trial-arm with parameters
    arms_df = pd.DataFrame()
    for trial_index, trial in exp.trials.items():
        for arm in trial.arms:
            arms_df = arms_df.append(
                {"arm_name": arm.name, "trial_index": trial_index, **arm.parameters},
                ignore_index=True,
            )

    # Fetch results; in case arms_df is empty, return empty results (legacy behavior)
    results = exp.fetch_data(metrics, **kwargs).df
    if len(arms_df.index) == 0:
        if len(results.index) != 0:
            raise ValueError(
                "exp.fetch_data().df returned more rows than there are experimental "
                "arms. This is an inconsistent experimental state. Please report to "
                "Ax support."
            )
        return results

    # Create key column from key_components
    arms_df["trial_index"] = arms_df["trial_index"].astype(int)
    key_col = "-".join(key_components)
    key_vals = arms_df[key_components[0]].astype("str") + arms_df[
        key_components[1]
    ].astype("str")
    arms_df[key_col] = key_vals

    # Add trial status
    trials = exp.trials.items()
    trial_to_status = {index: trial.status.name for index, trial in trials}
    arms_df["trial_status"] = [
        trial_to_status[trial_index] for trial_index in arms_df.trial_index
    ]

    # Add and generator_run model keys
    arms_df["generator_model"] = [
        # This accounts for the generic case that generator_runs is a list of arbitrary
        # length. If all elements are `None`, this yields an empty string. Repeated
        # generator models within a trial are condensed via a set comprehension.
        ", ".join(
            {
                not_none(generator_run._model_key)
                for generator_run in exp.trials[trial_index].generator_runs
                if generator_run._model_key is not None
            }
        )
        if trial_index in exp.trials
        else ""
        for trial_index in arms_df.trial_index
    ]

    # replace all unknown generator_models (denoted by empty strings) with "Unknown"
    arms_df["generator_model"] = [
        "Unknown" if generator_model == "" else generator_model
        for generator_model in arms_df["generator_model"]
    ]

    # Add any run_metadata fields to arms_df
    if run_metadata_fields is not None:
        if not (
            isinstance(run_metadata_fields, list)
            and all(isinstance(field, str) for field in run_metadata_fields)
        ):
            raise ValueError(
                "run_metadata_fields must be List[str] or None. "
                f"Got {run_metadata_fields}"
            )

        # add additional run_metadata fields
        for field in run_metadata_fields:
            trial_to_metadata_field = {
                index: (
                    trial.run_metadata[field] if field in trial.run_metadata else None
                )
                for index, trial in trials
            }
            if any(trial_to_metadata_field.values()):  # field present for any trial
                if not all(
                    trial_to_metadata_field.values()
                ):  # not present for all trials
                    logger.warning(
                        f"Field {field} missing for some trials' run_metadata. "
                        "Returning None when missing."
                    )
                arms_df[field] = [
                    trial_to_metadata_field[key] for key in arms_df.trial_index
                ]
            else:
                logger.warning(
                    f"Field {field} missing for all trials' run_metadata. "
                    "Not appending column."
                )

    if len(results.index) == 0:
        logger.info(
            f"No results present for the specified metrics `{metrics}`. "
            "Returning arm parameters and metadata only."
        )
        exp_df = arms_df
    elif not all(col in results.columns for col in key_components):
        logger.warn(
            f"At least one of key columns `{key_components}` not present in results df "
            f"`{results}`. Returning arm parameters and metadata only."
        )
        exp_df = arms_df
    else:
        # prepare results for merge
        key_vals = results[key_components[0]].astype("str") + results[
            key_components[1]
        ].astype("str")
        results[key_col] = key_vals
        metric_vals = results.pivot(
            index=key_col, columns="metric_name", values="mean"
        ).reset_index()

        # dedupe results by key_components
        metadata = results[key_components + [key_col]].drop_duplicates()
        metrics_df = pd.merge(metric_vals, metadata, on=key_col)

        # merge and return
        exp_df = pd.merge(
            metrics_df, arms_df, on=key_components + [key_col], how="outer"
        )
    return prep_return(df=exp_df, drop_col=key_col, sort_by=["arm_name"])


def get_best_trial(
    exp: Experiment,
    additional_metrics: Optional[List[Metric]] = None,
    run_metadata_fields: Optional[List[str]] = None,
    **kwargs: Any,
) -> Optional[pd.DataFrame]:
    """Finds the optimal trial given an experiment, based on raw objective value.

    Returns a 1-row dataframe. Should match the row of ``exp_to_df`` with the best
    raw objective value, given the same arguments.

    Args:
        exp: An Experiment that may have pending trials.
        additional_metrics: List of metrics to return in addition to the objective
            metric. Return all metrics if None.
        run_metadata_fields: fields to extract from trial.run_metadata for trial
            in experiment.trials. If there are multiple arms per trial, these
            fields will be replicated across the arms of a trial.
        **kwargs: Custom named arguments, useful for passing complex
            objects from call-site to the `fetch_data` callback.

    Returns:
        DataFrame: A dataframe of inputs and metrics of the optimal trial.
    """
    objective = not_none(exp.optimization_config).objective
    if isinstance(objective, MultiObjective):
        logger.warning(
            "No best trial is available for `MultiObjective` optimization. "
            "Returning None for best trial."
        )
        return None
    if isinstance(objective, ScalarizedObjective):
        logger.warning(
            "No best trial is available for `ScalarizedObjective` optimization. "
            "Returning None for best trial."
        )
        return None
    if (additional_metrics is not None) and (
        objective.metric not in additional_metrics
    ):
        additional_metrics.append(objective.metric)
    trials_df = exp_to_df(
        exp=exp,
        metrics=additional_metrics,
        run_metadata_fields=run_metadata_fields,
        **kwargs,
    )
    if len(trials_df.index) == 0:
        logger.warning("`exp_to_df` returned 0 trials. Returning None for best trial.")
        return None

    metric_name = objective.metric.name
    minimize = objective.minimize
    if metric_name not in trials_df.columns:
        logger.warning(
            f"`exp_to_df` did not have data for metric {metric_name}. "
            "Returning None for best trial."
        )
        return None

    metric_optimum = (
        trials_df[metric_name].min() if minimize else trials_df[metric_name].max()
    )
    return pd.DataFrame(trials_df[trials_df[metric_name] == metric_optimum].head(1))
