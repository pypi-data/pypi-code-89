from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.allergyintolerance import AllergyIntoleranceSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # clinicalStatus (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for clinicalStatus
    from spark_auto_mapper_fhir.value_sets.allergy_intolerance_clinical_status_codes import (
        AllergyIntoleranceClinicalStatusCodesCode,
    )

    # End Import for CodeableConcept for clinicalStatus
    # verificationStatus (CodeableConcept)
    # Import for CodeableConcept for verificationStatus
    from spark_auto_mapper_fhir.value_sets.allergy_intolerance_verification_status_codes import (
        AllergyIntoleranceVerificationStatusCodesCode,
    )

    # End Import for CodeableConcept for verificationStatus
    # type_ (AllergyIntoleranceType)
    from spark_auto_mapper_fhir.value_sets.allergy_intolerance_type import (
        AllergyIntoleranceTypeCode,
    )

    # category (AllergyIntoleranceCategory)
    from spark_auto_mapper_fhir.value_sets.allergy_intolerance_category import (
        AllergyIntoleranceCategoryCode,
    )

    # criticality (AllergyIntoleranceCriticality)
    from spark_auto_mapper_fhir.value_sets.allergy_intolerance_criticality import (
        AllergyIntoleranceCriticalityCode,
    )

    # code (CodeableConcept)
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.allergy_intolerance_substance_or__product__condition_and_negation_codes import (
        AllergyIntoleranceSubstance_or_Product_ConditionAndNegationCodesCode,
    )

    # End Import for CodeableConcept for code
    # patient (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # recordedDate (dateTime)
    # recorder (Reference)
    # Imports for References for recorder
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # asserter (Reference)
    # Imports for References for asserter
    # lastOccurrence (dateTime)
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # reaction (AllergyIntolerance.Reaction)
    from spark_auto_mapper_fhir.backbone_elements.allergy_intolerance_reaction import (
        AllergyIntoleranceReaction,
    )

    # onsetDateTime (dateTime)
    # onsetAge (Age)
    from spark_auto_mapper_fhir.complex_types.age import Age

    # onsetPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # onsetRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # onsetString (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AllergyIntolerance(FhirResourceBase):
    """
    AllergyIntolerance
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        clinicalStatus: Optional[
            CodeableConcept[AllergyIntoleranceClinicalStatusCodesCode]
        ] = None,
        verificationStatus: Optional[
            CodeableConcept[AllergyIntoleranceVerificationStatusCodesCode]
        ] = None,
        type_: Optional[AllergyIntoleranceTypeCode] = None,
        category: Optional[FhirList[AllergyIntoleranceCategoryCode]] = None,
        criticality: Optional[AllergyIntoleranceCriticalityCode] = None,
        code: Optional[
            CodeableConcept[
                AllergyIntoleranceSubstance_or_Product_ConditionAndNegationCodesCode
            ]
        ] = None,
        patient: Reference[Union[Patient]],
        encounter: Optional[Reference[Union[Encounter]]] = None,
        recordedDate: Optional[FhirDateTime] = None,
        recorder: Optional[
            Reference[Union[Practitioner, PractitionerRole, Patient, RelatedPerson]]
        ] = None,
        asserter: Optional[
            Reference[Union[Patient, RelatedPerson, Practitioner, PractitionerRole]]
        ] = None,
        lastOccurrence: Optional[FhirDateTime] = None,
        note: Optional[FhirList[Annotation]] = None,
        reaction: Optional[FhirList[AllergyIntoleranceReaction]] = None,
        onsetDateTime: Optional[FhirDateTime] = None,
        onsetAge: Optional[Age] = None,
        onsetPeriod: Optional[Period] = None,
        onsetRange: Optional[Range] = None,
        onsetString: Optional[FhirString] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Business identifiers assigned to this AllergyIntolerance by the performer or
        other systems which remain constant as the resource is updated and propagates
        from server to server.
            :param clinicalStatus: The clinical status of the allergy or intolerance.
            :param verificationStatus: Assertion about certainty associated with the propensity, or potential risk,
        of a reaction to the identified substance (including pharmaceutical product).
            :param type_: Identification of the underlying physiological mechanism for the reaction
        risk.
            :param category: Category of the identified substance.
            :param criticality: Estimate of the potential clinical harm, or seriousness, of the reaction to
        the identified substance.
            :param code: Code for an allergy or intolerance statement (either a positive or a
        negated/excluded statement).  This may be a code for a substance or
        pharmaceutical product that is considered to be responsible for the adverse
        reaction risk (e.g., "Latex"), an allergy or intolerance condition (e.g.,
        "Latex allergy"), or a negated/excluded code for a specific substance or class
        (e.g., "No latex allergy") or a general or categorical negated statement
        (e.g.,  "No known allergy", "No known drug allergies").  Note: the substance
        for a specific reaction may be different from the substance identified as the
        cause of the risk, but it must be consistent with it. For instance, it may be
        a more specific substance (e.g. a brand medication) or a composite product
        that includes the identified substance. It must be clinically safe to only
        process the 'code' and ignore the 'reaction.substance'.  If a receiving system
        is unable to confirm that AllergyIntolerance.reaction.substance falls within
        the semantic scope of AllergyIntolerance.code, then the receiving system
        should ignore AllergyIntolerance.reaction.substance.
            :param patient: The patient who has the allergy or intolerance.
            :param encounter: The encounter when the allergy or intolerance was asserted.
            :param recordedDate: The recordedDate represents when this particular AllergyIntolerance record was
        created in the system, which is often a system-generated date.
            :param recorder: Individual who recorded the record and takes responsibility for its content.
            :param asserter: The source of the information about the allergy that is recorded.
            :param lastOccurrence: Represents the date and/or time of the last known occurrence of a reaction
        event.
            :param note: Additional narrative about the propensity for the Adverse Reaction, not
        captured in other fields.
            :param reaction: Details about each adverse reaction event linked to exposure to the identified
        substance.
            :param onsetDateTime: None
            :param onsetAge: None
            :param onsetPeriod: None
            :param onsetRange: None
            :param onsetString: None
        """
        super().__init__(
            resourceType="AllergyIntolerance",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            clinicalStatus=clinicalStatus,
            verificationStatus=verificationStatus,
            type_=type_,
            category=category,
            criticality=criticality,
            code=code,
            patient=patient,
            encounter=encounter,
            recordedDate=recordedDate,
            recorder=recorder,
            asserter=asserter,
            lastOccurrence=lastOccurrence,
            note=note,
            reaction=reaction,
            onsetDateTime=onsetDateTime,
            onsetAge=onsetAge,
            onsetPeriod=onsetPeriod,
            onsetRange=onsetRange,
            onsetString=onsetString,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return AllergyIntoleranceSchema.get_schema(include_extension=include_extension)
