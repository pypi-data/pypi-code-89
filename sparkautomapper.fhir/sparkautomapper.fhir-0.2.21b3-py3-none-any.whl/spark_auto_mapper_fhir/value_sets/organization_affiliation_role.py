from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class OrganizationAffiliationRoleCode(FhirValueSetBase):
    """
    OrganizationAffiliationRole
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/organization-role
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/organization-role"


class OrganizationAffiliationRoleCodeValues:
    """
    None
    """

    Provider = OrganizationAffiliationRoleCode("provider")
    """
    An organization such as a public health agency, community/social services provider, etc.
    """
    Agency = OrganizationAffiliationRoleCode("agency")
    """
    An organization providing research-related services such as conducting research, recruiting research participants, analyzing data, etc.
    """
    Research = OrganizationAffiliationRoleCode("research")
    """
    An organization providing reimbursement, payment, or related services
    """
    Payer = OrganizationAffiliationRoleCode("payer")
    """
    An organization providing diagnostic testing/laboratory services
    """
    Diagnostics = OrganizationAffiliationRoleCode("diagnostics")
    """
    An organization that provides medical supplies (e.g. medical devices, equipment, pharmaceutical products, etc.)
    """
    Supplier = OrganizationAffiliationRoleCode("supplier")
    """
    An organization that facilitates electronic clinical data exchange between entities
    """
    HIE_HIO = OrganizationAffiliationRoleCode("HIE/HIO")
    """
    A type of non-ownership relationship between entities (encompasses partnerships, collaboration, joint ventures, etc.)
    """
    Member = OrganizationAffiliationRoleCode("member")
