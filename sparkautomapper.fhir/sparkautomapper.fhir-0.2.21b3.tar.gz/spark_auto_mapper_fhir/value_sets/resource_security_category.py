from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ResourceSecurityCategoryCode(FhirValueSetBase):
    """
    ResourceSecurityCategory
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/resource-security-category
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/resource-security-category"


class ResourceSecurityCategoryCodeValues:
    """
    These resources tend to not contain any individual data, or business sensitive data. Most often these Resources will be available for anonymous access, meaning there is no access control based on the user or system requesting. However these Resources do tend to contain important information that must be authenticated back to the source publishing them, and protected from integrity failures in communication. For this reason server authenticated https (TLS) is recommended to provide authentication of the server and integrity protection in transit. This is normal web-server use of https.
    """

    AnonymousREADAccessResource = ResourceSecurityCategoryCode("anonymous")
    """
    These Resources tend to not contain any individual data, but do have data that describe business or service sensitive data. The use of the term Business is not intended to only mean an incorporated business, but rather the more broad concept of an organization, location, or other group that is not identifable as individuals. Often these resources will require some for of client authentication to assure that only authorized access is given. The client access control may be to individuals, or may be to system identity. For this purpose possible client authentication methods such as: mutual-authenticated-TLS, APIKey, App signed JWT, or App OAuth client-id JWT For example: a App that uses a Business protected Provider Directory to determine other business endpoint details.
    """
    BusinessSensitiveResource = ResourceSecurityCategoryCode("business")
    """
    These Resources do NOT contain Patient data, but do contain individual information about other participants. These other individuals are Practitioners, PractionerRole, CareTeam, or other users. These identities are needed to enable the practice of healthcare. These identities are identities under general privacy regulations, and thus must consider Privacy risk. Often access to these other identities are covered by business relationships. For this purpose access to these Resources will tend to be Role specific using methods such as RBAC or ABAC.
    """
    IndividualSensitiveResource = ResourceSecurityCategoryCode("individual")
    """
    These Resources make up the bulk of FHIR and therefore are the most commonly understood. These Resources contain highly sesitive health information, or are closely linked to highly sensitive health information. These Resources will often use the security labels to differentiate various confidentiality levels within this broad group of Patient Sensitive data. Access to these Resources often requires a declared Purpose Of Use. Access to these Resources is often controlled by a Privacy Consent.
    """
    PatientSensitive = ResourceSecurityCategoryCode("patient")
    """
    Some Resources can be used for a wide scope of use-cases that span very sensitive to very non-sensitive. These Resources do not fall into any of the above classifications, as their sensitivity is highly variable. These Resources will need special handling. These Resources often contain metadata that describes the content in a way that can be used for Access Control decisions.
    """
    NotClassified = ResourceSecurityCategoryCode("not-classified")
