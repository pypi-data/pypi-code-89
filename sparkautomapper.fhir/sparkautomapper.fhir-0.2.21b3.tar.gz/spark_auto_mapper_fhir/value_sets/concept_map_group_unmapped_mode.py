from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConceptMapGroupUnmappedModeCode(FhirValueSetBase):
    """
    ConceptMapGroupUnmappedMode
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/conceptmap-unmapped-mode
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/conceptmap-unmapped-mode"


class ConceptMapGroupUnmappedModeCodeValues:
    """
    Use the code as provided in the $translate request.
    """

    ProvidedCode = ConceptMapGroupUnmappedModeCode("provided")
    """
    Use the code explicitly provided in the group.unmapped.
    """
    FixedCode = ConceptMapGroupUnmappedModeCode("fixed")
    """
    Use the map identified by the canonical URL in the url element.
    """
    OtherMap = ConceptMapGroupUnmappedModeCode("other-map")
