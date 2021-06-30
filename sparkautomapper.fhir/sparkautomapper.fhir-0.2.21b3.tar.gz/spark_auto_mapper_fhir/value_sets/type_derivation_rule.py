from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TypeDerivationRuleCode(FhirValueSetBase):
    """
    TypeDerivationRule
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/type-derivation-rule
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/type-derivation-rule"


class TypeDerivationRuleCodeValues:
    """
    This definition defines a new type that adds additional elements to the base type.
    """

    Specialization = TypeDerivationRuleCode("specialization")
    """
    This definition adds additional rules to an existing concrete type.
    """
    Constraint = TypeDerivationRuleCode("constraint")
