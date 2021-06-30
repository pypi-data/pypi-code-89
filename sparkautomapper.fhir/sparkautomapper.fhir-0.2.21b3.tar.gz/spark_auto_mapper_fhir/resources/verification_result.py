from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.verificationresult import VerificationResultSchema

if TYPE_CHECKING:
    pass
    # target (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for target
    from spark_auto_mapper_fhir.resources.resource import Resource

    # targetLocation (string)
    # need (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for need
    from spark_auto_mapper_fhir.value_sets.need import NeedCode

    # End Import for CodeableConcept for need
    # status (status)
    from spark_auto_mapper_fhir.value_sets.status import StatusCode

    # statusDate (dateTime)
    # validationType (CodeableConcept)
    # Import for CodeableConcept for validationType
    from spark_auto_mapper_fhir.value_sets.validation_type import Validation_typeCode

    # End Import for CodeableConcept for validationType
    # validationProcess (CodeableConcept)
    # Import for CodeableConcept for validationProcess
    from spark_auto_mapper_fhir.value_sets.validation_process import (
        Validation_processCode,
    )

    # End Import for CodeableConcept for validationProcess
    # frequency (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # lastPerformed (dateTime)
    # nextScheduled (date)
    # failureAction (CodeableConcept)
    # Import for CodeableConcept for failureAction
    from spark_auto_mapper_fhir.value_sets.failure_action import Failure_actionCode

    # End Import for CodeableConcept for failureAction
    # primarySource (VerificationResult.PrimarySource)
    from spark_auto_mapper_fhir.backbone_elements.verification_result_primary_source import (
        VerificationResultPrimarySource,
    )

    # attestation (VerificationResult.Attestation)
    from spark_auto_mapper_fhir.backbone_elements.verification_result_attestation import (
        VerificationResultAttestation,
    )

    # validator (VerificationResult.Validator)
    from spark_auto_mapper_fhir.backbone_elements.verification_result_validator import (
        VerificationResultValidator,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class VerificationResult(FhirResourceBase):
    """
    VerificationResult
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        target: Optional[FhirList[Reference[Union[Resource]]]] = None,
        targetLocation: Optional[FhirList[FhirString]] = None,
        need: Optional[CodeableConcept[NeedCode]] = None,
        status: StatusCode,
        statusDate: Optional[FhirDateTime] = None,
        validationType: Optional[CodeableConcept[Validation_typeCode]] = None,
        validationProcess: Optional[
            FhirList[CodeableConcept[Validation_processCode]]
        ] = None,
        frequency: Optional[Timing] = None,
        lastPerformed: Optional[FhirDateTime] = None,
        nextScheduled: Optional[FhirDate] = None,
        failureAction: Optional[CodeableConcept[Failure_actionCode]] = None,
        primarySource: Optional[FhirList[VerificationResultPrimarySource]] = None,
        attestation: Optional[VerificationResultAttestation] = None,
        validator: Optional[FhirList[VerificationResultValidator]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param target: A resource that was validated.
            :param targetLocation: The fhirpath location(s) within the resource that was validated.
            :param need: The frequency with which the target must be validated (none; initial;
        periodic).
            :param status: The validation status of the target (attested; validated; in process; requires
        revalidation; validation failed; revalidation failed).
            :param statusDate: When the validation status was updated.
            :param validationType: What the target is validated against (nothing; primary source; multiple
        sources).
            :param validationProcess: The primary process by which the target is validated (edit check; value set;
        primary source; multiple sources; standalone; in context).
            :param frequency: Frequency of revalidation.
            :param lastPerformed: The date/time validation was last completed (including failed validations).
            :param nextScheduled: The date when target is next validated, if appropriate.
            :param failureAction: The result if validation fails (fatal; warning; record only; none).
            :param primarySource: Information about the primary source(s) involved in validation.
            :param attestation: Information about the entity attesting to information.
            :param validator: Information about the entity validating information.
        """
        super().__init__(
            resourceType="VerificationResult",
            id_=id_,
            meta=meta,
            extension=extension,
            target=target,
            targetLocation=targetLocation,
            need=need,
            status=status,
            statusDate=statusDate,
            validationType=validationType,
            validationProcess=validationProcess,
            frequency=frequency,
            lastPerformed=lastPerformed,
            nextScheduled=nextScheduled,
            failureAction=failureAction,
            primarySource=primarySource,
            attestation=attestation,
            validator=validator,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return VerificationResultSchema.get_schema(include_extension=include_extension)
