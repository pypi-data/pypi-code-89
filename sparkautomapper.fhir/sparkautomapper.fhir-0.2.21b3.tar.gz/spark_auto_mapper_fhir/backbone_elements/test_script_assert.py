from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # label (string)
    # description (string)
    # direction (AssertionDirectionType)
    from spark_auto_mapper_fhir.value_sets.assertion_direction_type import (
        AssertionDirectionTypeCode,
    )

    # compareToSourceId (string)
    # compareToSourceExpression (string)
    # compareToSourcePath (string)
    # contentType (code)
    from spark_auto_mapper_fhir.complex_types.code import code

    # expression (string)
    # headerField (string)
    # minimumId (string)
    # navigationLinks (boolean)
    # operator (AssertionOperatorType)
    from spark_auto_mapper_fhir.value_sets.assertion_operator_type import (
        AssertionOperatorTypeCode,
    )

    # path (string)
    # requestMethod (TestScriptRequestMethodCode)
    from spark_auto_mapper_fhir.value_sets.test_script_request_method_code import (
        TestScriptRequestMethodCodeCode,
    )

    # requestURL (string)
    # resource (code)
    # response (AssertionResponseTypes)
    from spark_auto_mapper_fhir.value_sets.assertion_response_types import (
        AssertionResponseTypesCode,
    )

    # responseCode (string)
    # sourceId (id)
    from spark_auto_mapper_fhir.complex_types.id import id

    # validateProfileId (id)
    # value (string)
    # warningOnly (boolean)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestScriptAssert(FhirBackboneElementBase):
    """
    TestScript.Assert
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        label: Optional[FhirString] = None,
        description: Optional[FhirString] = None,
        direction: Optional[AssertionDirectionTypeCode] = None,
        compareToSourceId: Optional[FhirString] = None,
        compareToSourceExpression: Optional[FhirString] = None,
        compareToSourcePath: Optional[FhirString] = None,
        contentType: Optional[code] = None,
        expression: Optional[FhirString] = None,
        headerField: Optional[FhirString] = None,
        minimumId: Optional[FhirString] = None,
        navigationLinks: Optional[FhirBoolean] = None,
        operator: Optional[AssertionOperatorTypeCode] = None,
        path: Optional[FhirString] = None,
        requestMethod: Optional[TestScriptRequestMethodCodeCode] = None,
        requestURL: Optional[FhirString] = None,
        resource: Optional[code] = None,
        response: Optional[AssertionResponseTypesCode] = None,
        responseCode: Optional[FhirString] = None,
        sourceId: Optional[id] = None,
        validateProfileId: Optional[id] = None,
        value: Optional[FhirString] = None,
        warningOnly: FhirBoolean,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param label: The label would be used for tracking/logging purposes by test engines.
            :param description: The description would be used by test engines for tracking and reporting
        purposes.
            :param direction: The direction to use for the assertion.
            :param compareToSourceId: Id of the source fixture used as the contents to be evaluated by either the
        "source/expression" or "sourceId/path" definition.
            :param compareToSourceExpression: The FHIRPath expression to evaluate against the source fixture. When
        compareToSourceId is defined, either compareToSourceExpression or
        compareToSourcePath must be defined, but not both.
            :param compareToSourcePath: XPath or JSONPath expression to evaluate against the source fixture. When
        compareToSourceId is defined, either compareToSourceExpression or
        compareToSourcePath must be defined, but not both.
            :param contentType: The mime-type contents to compare against the request or response message
        'Content-Type' header.
            :param expression: The FHIRPath expression to be evaluated against the request or response
        message contents - HTTP headers and payload.
            :param headerField: The HTTP header field name e.g. 'Location'.
            :param minimumId: The ID of a fixture.  Asserts that the response contains at a minimum the
        fixture specified by minimumId.
            :param navigationLinks: Whether or not the test execution performs validation on the bundle navigation
        links.
            :param operator: The operator type defines the conditional behavior of the assert. If not
        defined, the default is equals.
            :param path: The XPath or JSONPath expression to be evaluated against the fixture
        representing the response received from server.
            :param requestMethod: The request method or HTTP operation code to compare against that used by the
        client system under test.
            :param requestURL: The value to use in a comparison against the request URL path string.
            :param resource: The type of the resource.  See http://build.fhir.org/resourcelist.html.
            :param response: okay | created | noContent | notModified | bad | forbidden | notFound |
        methodNotAllowed | conflict | gone | preconditionFailed | unprocessable.
            :param responseCode: The value of the HTTP response code to be tested.
            :param sourceId: Fixture to evaluate the XPath/JSONPath expression or the headerField  against.
            :param validateProfileId: The ID of the Profile to validate against.
            :param value: The value to compare to.
            :param warningOnly: Whether or not the test execution will produce a warning only on error for
        this assert.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            label=label,
            description=description,
            direction=direction,
            compareToSourceId=compareToSourceId,
            compareToSourceExpression=compareToSourceExpression,
            compareToSourcePath=compareToSourcePath,
            contentType=contentType,
            expression=expression,
            headerField=headerField,
            minimumId=minimumId,
            navigationLinks=navigationLinks,
            operator=operator,
            path=path,
            requestMethod=requestMethod,
            requestURL=requestURL,
            resource=resource,
            response=response,
            responseCode=responseCode,
            sourceId=sourceId,
            validateProfileId=validateProfileId,
            value=value,
            warningOnly=warningOnly,
        )
