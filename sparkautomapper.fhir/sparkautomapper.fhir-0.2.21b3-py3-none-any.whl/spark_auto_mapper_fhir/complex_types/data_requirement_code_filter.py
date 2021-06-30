from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase

if TYPE_CHECKING:
    pass
    # path (string)
    # searchParam (string)
    # valueSet (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # code (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for code


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DataRequirementCodeFilter(FhirComplexTypeBase):
    """
    DataRequirement.CodeFilter
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        path: Optional[FhirString] = None,
        searchParam: Optional[FhirString] = None,
        valueSet: Optional[FhirCanonical] = None,
        code: Optional[FhirList[Coding[GenericTypeCode]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param path: The code-valued attribute of the filter. The specified path SHALL be a
        FHIRPath resolveable on the specified type of the DataRequirement, and SHALL
        consist only of identifiers, constant indexers, and .resolve(). The path is
        allowed to contain qualifiers (.) to traverse sub-elements, as well as
        indexers ([x]) to traverse multiple-cardinality sub-elements (see the [Simple
        FHIRPath Profile](fhirpath.html#simple) for full details). Note that the index
        must be an integer constant. The path must resolve to an element of type code,
        Coding, or CodeableConcept.
            :param searchParam: A token parameter that refers to a search parameter defined on the specified
        type of the DataRequirement, and which searches on elements of type code,
        Coding, or CodeableConcept.
            :param valueSet: The valueset for the code filter. The valueSet and code elements are additive.
        If valueSet is specified, the filter will return only those data items for
        which the value of the code-valued element specified in the path is a member
        of the specified valueset.
            :param code: The codes for the code filter. If values are given, the filter will return
        only those data items for which the code-valued attribute specified by the
        path has a value that is one of the specified codes. If codes are specified in
        addition to a value set, the filter returns items matching a code in the value
        set or one of the specified codes.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            path=path,
            searchParam=searchParam,
            valueSet=valueSet,
            code=code,
        )
