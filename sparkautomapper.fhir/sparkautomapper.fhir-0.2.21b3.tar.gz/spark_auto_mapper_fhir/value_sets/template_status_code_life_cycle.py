from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TemplateStatusCodeLifeCycleCode(FhirValueSetBase):
    """
    TemplateStatusCodeLifeCycle
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    urn:oid:2.16.840.1.113883.3.1937.98.11.8
    """
    codeset: FhirUri = "urn:oid:2.16.840.1.113883.3.1937.98.11.8"


class TemplateStatusCodeLifeCycleCodeValues:
    """
    Design is under development (nascent).
    """

    Draft = TemplateStatusCodeLifeCycleCode("draft")
    """
    Design is completed and is being reviewed.
    """
    UnderPre_publicationReview = TemplateStatusCodeLifeCycleCode("pending")
    """
    Design has been deemed fit for the intended purpose and is published by the governance group.
    """
    Active = TemplateStatusCodeLifeCycleCode("active")
    """
    Design is active, but is under review. The review may result in a change to the design. The change may necessitate a new version to be created. This in turn may result in the prior version of the template to be retired. Alternatively, the review may result in a change to the design that does not require a new version to be created, or it may result in no change to the design at all.
    """
    InReview = TemplateStatusCodeLifeCycleCode("review")
    """
    A drafted design is determined to be erroneous or not fit for intended purpose and is discontinued before ever being published in an active state.
    """
    Cancelled = TemplateStatusCodeLifeCycleCode("cancelled")
    """
    A previously drafted design is determined to be erroneous or not fit for intended purpose and is discontinued before ever being published for consideration in a pending state.
    """
    Rejected = TemplateStatusCodeLifeCycleCode("rejected")
    """
    A previously active design is discontinued from use. It should no longer be used for future designs, but for historical purposes may be used to process data previously recorded using this design. A newer design may or may not exist. The design is published in the retired state.
    """
    Retired = TemplateStatusCodeLifeCycleCode("retired")
    """
    A design is determined to be erroneous or not fit for the intended purpose and should no longer be used, even for historical purposes. No new designs can be developed for this template. The associated template no longer needs to be published, but if published, is shown in the terminated state.
    """
    Terminated = TemplateStatusCodeLifeCycleCode("terminated")
