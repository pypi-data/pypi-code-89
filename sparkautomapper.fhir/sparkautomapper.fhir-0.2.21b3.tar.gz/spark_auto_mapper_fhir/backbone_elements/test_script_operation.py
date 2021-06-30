from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
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
    # type_ (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.test_script_operation_code import (
        TestScriptOperationCodeCode,
    )

    # End Import for CodeableConcept for type_
    # resource (FHIRDefinedType)
    from spark_auto_mapper_fhir.value_sets.fhir_defined_type import FHIRDefinedTypeCode

    # label (string)
    # description (string)
    # accept (Mime Types)
    from spark_auto_mapper_fhir.value_sets.mime_types import MimeTypesCode

    # contentType (Mime Types)
    # destination (integer)
    # encodeRequestUrl (boolean)
    # method (TestScriptRequestMethodCode)
    from spark_auto_mapper_fhir.value_sets.test_script_request_method_code import (
        TestScriptRequestMethodCodeCode,
    )

    # origin (integer)
    # params (string)
    # requestHeader (TestScript.RequestHeader)
    from spark_auto_mapper_fhir.backbone_elements.test_script_request_header import (
        TestScriptRequestHeader,
    )

    # requestId (id)
    from spark_auto_mapper_fhir.complex_types.id import id

    # responseId (id)
    # sourceId (id)
    # targetId (id)
    # url (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestScriptOperation(FhirBackboneElementBase):
    """
    TestScript.Operation
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: Optional[Coding[TestScriptOperationCodeCode]] = None,
        resource: Optional[FHIRDefinedTypeCode] = None,
        label: Optional[FhirString] = None,
        description: Optional[FhirString] = None,
        accept: Optional[MimeTypesCode] = None,
        contentType: Optional[MimeTypesCode] = None,
        destination: Optional[FhirInteger] = None,
        encodeRequestUrl: FhirBoolean,
        method: Optional[TestScriptRequestMethodCodeCode] = None,
        origin: Optional[FhirInteger] = None,
        params: Optional[FhirString] = None,
        requestHeader: Optional[FhirList[TestScriptRequestHeader]] = None,
        requestId: Optional[id] = None,
        responseId: Optional[id] = None,
        sourceId: Optional[id] = None,
        targetId: Optional[id] = None,
        url: Optional[FhirString] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param type_: Server interaction or operation type.
            :param resource: The type of the resource.  See http://build.fhir.org/resourcelist.html.
            :param label: The label would be used for tracking/logging purposes by test engines.
            :param description: The description would be used by test engines for tracking and reporting
        purposes.
            :param accept: The mime-type to use for RESTful operation in the 'Accept' header.
            :param contentType: The mime-type to use for RESTful operation in the 'Content-Type' header.
            :param destination: The server where the request message is destined for.  Must be one of the
        server numbers listed in TestScript.destination section.
            :param encodeRequestUrl: Whether or not to implicitly send the request url in encoded format. The
        default is true to match the standard RESTful client behavior. Set to false
        when communicating with a server that does not support encoded url paths.
            :param method: The HTTP method the test engine MUST use for this operation regardless of any
        other operation details.
            :param origin: The server where the request message originates from.  Must be one of the
        server numbers listed in TestScript.origin section.
            :param params: Path plus parameters after [type].  Used to set parts of the request URL
        explicitly.
            :param requestHeader: Header elements would be used to set HTTP headers.
            :param requestId: The fixture id (maybe new) to map to the request.
            :param responseId: The fixture id (maybe new) to map to the response.
            :param sourceId: The id of the fixture used as the body of a PUT or POST request.
            :param targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET
        requests.
            :param url: Complete request URL.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            resource=resource,
            label=label,
            description=description,
            accept=accept,
            contentType=contentType,
            destination=destination,
            encodeRequestUrl=encodeRequestUrl,
            method=method,
            origin=origin,
            params=params,
            requestHeader=requestHeader,
            requestId=requestId,
            responseId=responseId,
            sourceId=sourceId,
            targetId=targetId,
            url=url,
        )
