from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # use (GraphCompartmentUse)
    from spark_auto_mapper_fhir.value_sets.graph_compartment_use import (
        GraphCompartmentUseCode,
    )

    # code (CompartmentType)
    from spark_auto_mapper_fhir.value_sets.compartment_type import CompartmentTypeCode

    # rule (GraphCompartmentRule)
    from spark_auto_mapper_fhir.value_sets.graph_compartment_rule import (
        GraphCompartmentRuleCode,
    )

    # expression (string)
    # description (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GraphDefinitionCompartment(FhirBackboneElementBase):
    """
    GraphDefinition.Compartment
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        use: GraphCompartmentUseCode,
        code: CompartmentTypeCode,
        rule: GraphCompartmentRuleCode,
        expression: Optional[FhirString] = None,
        description: Optional[FhirString] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param use: Defines how the compartment rule is used - whether it it is used to test
        whether resources are subject to the rule, or whether it is a rule that must
        be followed.
            :param code: Identifies the compartment.
            :param rule: identical | matching | different | no-rule | custom.
            :param expression: Custom rule, as a FHIRPath expression.
            :param description: Documentation for FHIRPath expression.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            use=use,
            code=code,
            rule=rule,
            expression=expression,
            description=description,
        )
