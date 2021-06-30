from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # name (code)
    from spark_auto_mapper_fhir.complex_types.code import code

    # use (OperationParameterUse)
    from spark_auto_mapper_fhir.value_sets.operation_parameter_use import (
        OperationParameterUseCode,
    )

    # min (integer)
    # max (string)
    # documentation (string)
    # type_ (FHIRAllTypes)
    from spark_auto_mapper_fhir.value_sets.fhir_all_types import FHIRAllTypesCode

    # targetProfile (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # searchType (SearchParamType)
    from spark_auto_mapper_fhir.value_sets.search_param_type import SearchParamTypeCode

    # binding (OperationDefinition.Binding)
    from spark_auto_mapper_fhir.backbone_elements.operation_definition_binding import (
        OperationDefinitionBinding,
    )

    # referencedFrom (OperationDefinition.ReferencedFrom)
    from spark_auto_mapper_fhir.backbone_elements.operation_definition_referenced_from import (
        OperationDefinitionReferencedFrom,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class OperationDefinitionParameter(FhirBackboneElementBase):
    """
    OperationDefinition.Parameter
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        name: code,
        use: OperationParameterUseCode,
        min: FhirInteger,
        max: FhirString,
        documentation: Optional[FhirString] = None,
        type_: Optional[FHIRAllTypesCode] = None,
        targetProfile: Optional[FhirList[FhirCanonical]] = None,
        searchType: Optional[SearchParamTypeCode] = None,
        binding: Optional[OperationDefinitionBinding] = None,
        referencedFrom: Optional[FhirList[OperationDefinitionReferencedFrom]] = None,
        part: Optional[FhirList[OperationDefinitionParameter]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param name: The name of used to identify the parameter.
            :param use: Whether this is an input or an output parameter.
            :param min: The minimum number of times this parameter SHALL appear in the request or
        response.
            :param max: The maximum number of times this element is permitted to appear in the request
        or response.
            :param documentation: Describes the meaning or use of this parameter.
            :param type_: The type for this parameter.
            :param targetProfile: Used when the type is "Reference" or "canonical", and identifies a profile
        structure or implementation Guide that applies to the target of the reference
        this parameter refers to. If any profiles are specified, then the content must
        conform to at least one of them. The URL can be a local reference - to a
        contained StructureDefinition, or a reference to another StructureDefinition
        or Implementation Guide by a canonical URL. When an implementation guide is
        specified, the target resource SHALL conform to at least one profile defined
        in the implementation guide.
            :param searchType: How the parameter is understood as a search parameter. This is only used if
        the parameter type is 'string'.
            :param binding: Binds to a value set if this parameter is coded (code, Coding,
        CodeableConcept).
            :param referencedFrom: Identifies other resource parameters within the operation invocation that are
        expected to resolve to this resource.
            :param part: The parts of a nested Parameter.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            name=name,
            use=use,
            min=min,
            max=max,
            documentation=documentation,
            type_=type_,
            targetProfile=targetProfile,
            searchType=searchType,
            binding=binding,
            referencedFrom=referencedFrom,
            part=part,
        )
