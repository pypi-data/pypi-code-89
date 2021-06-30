from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EndpointConnectionTypeCode(FhirValueSetBase):
    """
    EndpointConnectionType
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/endpoint-connection-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/endpoint-connection-type"


class EndpointConnectionTypeCodeValues:
    """
    IHE Cross Community Patient Discovery Profile (XCPD) - http://wiki.ihe.net/index.php/Cross-Community_Patient_Discovery
    """

    IHEXCPD = EndpointConnectionTypeCode("ihe-xcpd")
    """
    IHE Cross Community Access Profile (XCA) - http://wiki.ihe.net/index.php/Cross-Community_Access
    """
    IHEXCA = EndpointConnectionTypeCode("ihe-xca")
    """
    IHE Cross-Enterprise Document Reliable Exchange (XDR) - http://wiki.ihe.net/index.php/Cross-enterprise_Document_Reliable_Interchange
    """
    IHEXDR = EndpointConnectionTypeCode("ihe-xdr")
    """
    IHE Cross-Enterprise Document Sharing (XDS) - http://wiki.ihe.net/index.php/Cross-Enterprise_Document_Sharing
    """
    IHEXDS = EndpointConnectionTypeCode("ihe-xds")
    """
    IHE Invoke Image Display (IID) - http://wiki.ihe.net/index.php/Invoke_Image_Display
    """
    IHEIID = EndpointConnectionTypeCode("ihe-iid")
    """
    DICOMweb RESTful Image Retrieve - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.5.html
    """
    DICOMWADO_RS = EndpointConnectionTypeCode("dicom-wado-rs")
    """
    DICOMweb RESTful Image query - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.7.html
    """
    DICOMQIDO_RS = EndpointConnectionTypeCode("dicom-qido-rs")
    """
    DICOMweb RESTful image sending and storage - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.6.html
    """
    DICOMSTOW_RS = EndpointConnectionTypeCode("dicom-stow-rs")
    """
    DICOMweb Image Retrieve - http://dicom.nema.org/dicom/2013/output/chtml/part18/sect_6.3.html
    """
    DICOMWADO_URI = EndpointConnectionTypeCode("dicom-wado-uri")
    """
    Interact with the server interface using FHIR's RESTful interface. For details on its version/capabilities you should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement.
    """
    HL7FHIR = EndpointConnectionTypeCode("hl7-fhir-rest")
    """
    Use the servers FHIR Messaging interface. Details can be found on the messaging.html page in the FHIR Specification. The FHIR server's base address is specified in the Endpoint.address property.
    """
    HL7FHIRMessaging = EndpointConnectionTypeCode("hl7-fhir-msg")
    """
    HL7v2 messages over an LLP TCP connection
    """
    HL7V2MLLP = EndpointConnectionTypeCode("hl7v2-mllp")
    """
    Email delivery using a digital certificate to encrypt the content using the public key, receiver must have the private key to decrypt the content
    """
    SecureEmail = EndpointConnectionTypeCode("secure-email")
    """
    Direct Project information - http://wiki.directproject.org/
    """
    DirectProject = EndpointConnectionTypeCode("direct-project")
