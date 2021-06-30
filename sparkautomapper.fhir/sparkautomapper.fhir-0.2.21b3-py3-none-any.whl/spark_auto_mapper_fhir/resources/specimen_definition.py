from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.specimendefinition import SpecimenDefinitionSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # typeCollected (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for typeCollected
    from spark_auto_mapper_fhir.value_sets.v2_0487 import V2_0487

    # End Import for CodeableConcept for typeCollected
    # patientPreparation (CodeableConcept)
    # Import for CodeableConcept for patientPreparation
    from spark_auto_mapper_fhir.value_sets.prepare_patient import PreparePatientCode

    # End Import for CodeableConcept for patientPreparation
    # timeAspect (string)
    # collection (CodeableConcept)
    # Import for CodeableConcept for collection
    from spark_auto_mapper_fhir.value_sets.specimen_collection import (
        SpecimenCollectionCode,
    )

    # End Import for CodeableConcept for collection
    # typeTested (SpecimenDefinition.TypeTested)
    from spark_auto_mapper_fhir.backbone_elements.specimen_definition_type_tested import (
        SpecimenDefinitionTypeTested,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SpecimenDefinition(FhirResourceBase):
    """
    SpecimenDefinition
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        typeCollected: Optional[CodeableConcept[V2_0487]] = None,
        patientPreparation: Optional[
            FhirList[CodeableConcept[PreparePatientCode]]
        ] = None,
        timeAspect: Optional[FhirString] = None,
        collection: Optional[FhirList[CodeableConcept[SpecimenCollectionCode]]] = None,
        typeTested: Optional[FhirList[SpecimenDefinitionTypeTested]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param identifier: A business identifier associated with the kind of specimen.
        :param typeCollected: The kind of material to be collected.
        :param patientPreparation: Preparation of the patient for specimen collection.
        :param timeAspect: Time aspect of specimen collection (duration or offset).
        :param collection: The action to be performed for collecting the specimen.
        :param typeTested: Specimen conditioned in a container as expected by the testing laboratory.
        """
        super().__init__(
            resourceType="SpecimenDefinition",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            typeCollected=typeCollected,
            patientPreparation=patientPreparation,
            timeAspect=timeAspect,
            collection=collection,
            typeTested=typeTested,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return SpecimenDefinitionSchema.get_schema(include_extension=include_extension)
