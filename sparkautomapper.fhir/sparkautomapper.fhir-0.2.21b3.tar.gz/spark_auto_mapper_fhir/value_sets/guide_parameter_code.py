from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GuideParameterCodeCode(FhirValueSetBase):
    """
    GuideParameterCode
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/guide-parameter-code
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/guide-parameter-code"


class GuideParameterCodeCodeValues:
    """
    If the value of this string 0..* parameter is one of the metadata fields then all conformance resources will have any specified [Resource].[field] overwritten with the ImplementationGuide.[field], where field is one of: version, date, status, publisher, contact, copyright, experimental, jurisdiction, useContext.
    """

    ApplyMetadataValue = GuideParameterCodeCode("apply")
    """
    The value of this string 0..* parameter is a subfolder of the build context's location that is to be scanned to load resources. Scope is (if present) a particular resource type.
    """
    ResourcePath = GuideParameterCodeCode("path-resource")
    """
    The value of this string 0..1 parameter is a subfolder of the build context's location that contains files that are part of the html content processed by the builder.
    """
    PagesPath = GuideParameterCodeCode("path-pages")
    """
    The value of this string 0..1 parameter is a subfolder of the build context's location that is used as the terminology cache. If this is not present, the terminology cache is on the local system, not under version control.
    """
    TerminologyCachePath = GuideParameterCodeCode("path-tx-cache")
    """
    The value of this string 0..* parameter is a parameter (name=value) when expanding value sets for this implementation guide. This is particularly used to specify the versions of published terminologies such as SNOMED CT.
    """
    ExpansionProfile = GuideParameterCodeCode("expansion-parameter")
    """
    The value of this string 0..1 parameter is either "warning" or "error" (default = "error"). If the value is "warning" then IG build tools allow the IG to be considered successfully build even when there is no internal broken links.
    """
    BrokenLinksRule = GuideParameterCodeCode("rule-broken-links")
    """
    The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in XML format. If not present, the Publication Tool decides whether to generate XML.
    """
    GenerateXML = GuideParameterCodeCode("generate-xml")
    """
    The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in JSON format. If not present, the Publication Tool decides whether to generate JSON.
    """
    GenerateJSON = GuideParameterCodeCode("generate-json")
    """
    The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in Turtle format. If not present, the Publication Tool decides whether to generate Turtle.
    """
    GenerateTurtle = GuideParameterCodeCode("generate-turtle")
    """
    The value of this string singleton parameter is the name of the file to use as the builder template for each generated page (see templating).
    """
    HTMLTemplate = GuideParameterCodeCode("html-template")
