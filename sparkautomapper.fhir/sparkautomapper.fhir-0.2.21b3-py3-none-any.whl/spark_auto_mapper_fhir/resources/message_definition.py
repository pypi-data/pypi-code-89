from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.messagedefinition import MessageDefinitionSchema

if TYPE_CHECKING:
    pass
    # url (uri)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # version (string)
    # name (string)
    # title (string)
    # replaces (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # status (PublicationStatus)
    from spark_auto_mapper_fhir.value_sets.publication_status import (
        PublicationStatusCode,
    )

    # experimental (boolean)
    # date (dateTime)
    # publisher (string)
    # contact (ContactDetail)
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

    # description (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # useContext (UsageContext)
    from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext

    # jurisdiction (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for jurisdiction
    from spark_auto_mapper_fhir.value_sets.jurisdiction_value_set import (
        JurisdictionValueSetCode,
    )

    # End Import for CodeableConcept for jurisdiction
    # purpose (markdown)
    # copyright (markdown)
    # base (canonical)
    # parent (canonical)
    # category (MessageSignificanceCategory)
    from spark_auto_mapper_fhir.value_sets.message_significance_category import (
        MessageSignificanceCategoryCode,
    )

    # focus (MessageDefinition.Focus)
    from spark_auto_mapper_fhir.backbone_elements.message_definition_focus import (
        MessageDefinitionFocus,
    )

    # responseRequired (messageheader-response-request)
    from spark_auto_mapper_fhir.value_sets.messageheader_response_request import (
        Messageheader_response_requestCode,
    )

    # allowedResponse (MessageDefinition.AllowedResponse)
    from spark_auto_mapper_fhir.backbone_elements.message_definition_allowed_response import (
        MessageDefinitionAllowedResponse,
    )

    # graph (canonical)
    # eventCoding (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for eventCoding
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for eventCoding
    # eventUri (uri)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MessageDefinition(FhirResourceBase):
    """
    MessageDefinition
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        url: Optional[FhirUri] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        version: Optional[FhirString] = None,
        name: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        replaces: Optional[FhirList[FhirCanonical]] = None,
        status: PublicationStatusCode,
        experimental: Optional[FhirBoolean] = None,
        date: FhirDateTime,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: Optional[FhirMarkdown] = None,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[
            FhirList[CodeableConcept[JurisdictionValueSetCode]]
        ] = None,
        purpose: Optional[FhirMarkdown] = None,
        copyright: Optional[FhirMarkdown] = None,
        base: Optional[FhirCanonical] = None,
        parent: Optional[FhirList[FhirCanonical]] = None,
        category: Optional[MessageSignificanceCategoryCode] = None,
        focus: Optional[FhirList[MessageDefinitionFocus]] = None,
        responseRequired: Optional[Messageheader_response_requestCode] = None,
        allowedResponse: Optional[FhirList[MessageDefinitionAllowedResponse]] = None,
        graph: Optional[FhirList[FhirCanonical]] = None,
        eventCoding: Optional[Coding[GenericTypeCode]] = None,
        eventUri: Optional[FhirUri] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param url: The business identifier that is used to reference the MessageDefinition and
        *is* expected to be consistent from server to server.
            :param identifier: A formal identifier that is used to identify this message definition when it
        is represented in other formats, or referenced in a specification, model,
        design or an instance.
            :param version: The identifier that is used to identify this version of the message definition
        when it is referenced in a specification, model, design or instance. This is
        an arbitrary value managed by the message definition author and is not
        expected to be globally unique. For example, it might be a timestamp (e.g.
        yyyymmdd) if a managed version is not available. There is also no expectation
        that versions can be placed in a lexicographical sequence.
            :param name: A natural language name identifying the message definition. This name should
        be usable as an identifier for the module by machine processing applications
        such as code generation.
            :param title: A short, descriptive, user-friendly title for the message definition.
            :param replaces: A MessageDefinition that is superseded by this definition.
            :param status: The status of this message definition. Enables tracking the life-cycle of the
        content.
            :param experimental: A Boolean value to indicate that this message definition is authored for
        testing purposes (or education/evaluation/marketing) and is not intended to be
        used for genuine usage.
            :param date: The date  (and optionally time) when the message definition was published. The
        date must change when the business version changes and it must change if the
        status code changes. In addition, it should change when the substantive
        content of the message definition changes.
            :param publisher: The name of the organization or individual that published the message
        definition.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: A free text natural language description of the message definition from a
        consumer's perspective.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate message
        definition instances.
            :param jurisdiction: A legal or geographic region in which the message definition is intended to be
        used.
            :param purpose: Explanation of why this message definition is needed and why it has been
        designed as it has.
            :param copyright: A copyright statement relating to the message definition and/or its contents.
        Copyright statements are generally legal restrictions on the use and
        publishing of the message definition.
            :param base: The MessageDefinition that is the basis for the contents of this resource.
            :param parent: Identifies a protocol or workflow that this MessageDefinition represents a
        step in.
            :param category: The impact of the content of the message.
            :param focus: Identifies the resource (or resources) that are being addressed by the event.
        For example, the Encounter for an admit message or two Account records for a
        merge.
            :param responseRequired: Declare at a message definition level whether a response is required or only
        upon error or success, or never.
            :param allowedResponse: Indicates what types of messages may be sent as an application-level response
        to this message.
            :param graph: Canonical reference to a GraphDefinition. If a URL is provided, it is the
        canonical reference to a [[[GraphDefinition]]] that it controls what resources
        are to be added to the bundle when building the document. The GraphDefinition
        can also specify profiles that apply to the various resources.
            :param eventCoding: None
            :param eventUri: None
        """
        super().__init__(
            resourceType="MessageDefinition",
            id_=id_,
            meta=meta,
            extension=extension,
            url=url,
            identifier=identifier,
            version=version,
            name=name,
            title=title,
            replaces=replaces,
            status=status,
            experimental=experimental,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            copyright=copyright,
            base=base,
            parent=parent,
            category=category,
            focus=focus,
            responseRequired=responseRequired,
            allowedResponse=allowedResponse,
            graph=graph,
            eventCoding=eventCoding,
            eventUri=eventUri,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MessageDefinitionSchema.get_schema(include_extension=include_extension)
