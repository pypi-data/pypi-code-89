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
from spark_fhir_schemas.r4.resources.structuremap import StructureMapSchema

if TYPE_CHECKING:
    pass
    # url (uri)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # version (string)
    # name (string)
    # title (string)
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
    # structure (StructureMap.Structure)
    from spark_auto_mapper_fhir.backbone_elements.structure_map_structure import (
        StructureMapStructure,
    )

    # import_ (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # group (StructureMap.Group)
    from spark_auto_mapper_fhir.backbone_elements.structure_map_group import (
        StructureMapGroup,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class StructureMap(FhirResourceBase):
    """
    StructureMap
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        url: FhirUri,
        identifier: Optional[FhirList[Identifier]] = None,
        version: Optional[FhirString] = None,
        name: FhirString,
        title: Optional[FhirString] = None,
        status: PublicationStatusCode,
        experimental: Optional[FhirBoolean] = None,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: Optional[FhirMarkdown] = None,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[
            FhirList[CodeableConcept[JurisdictionValueSetCode]]
        ] = None,
        purpose: Optional[FhirMarkdown] = None,
        copyright: Optional[FhirMarkdown] = None,
        structure: Optional[FhirList[StructureMapStructure]] = None,
        import_: Optional[FhirList[FhirCanonical]] = None,
        group: FhirList[StructureMapGroup],
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param url: An absolute URI that is used to identify this structure map when it is
        referenced in a specification, model, design or an instance; also called its
        canonical identifier. This SHOULD be globally unique and SHOULD be a literal
        address at which at which an authoritative instance of this structure map is
        (or will be) published. This URL can be the target of a canonical reference.
        It SHALL remain the same when the structure map is stored on different
        servers.
            :param identifier: A formal identifier that is used to identify this structure map when it is
        represented in other formats, or referenced in a specification, model, design
        or an instance.
            :param version: The identifier that is used to identify this version of the structure map when
        it is referenced in a specification, model, design or instance. This is an
        arbitrary value managed by the structure map author and is not expected to be
        globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
        managed version is not available. There is also no expectation that versions
        can be placed in a lexicographical sequence.
            :param name: A natural language name identifying the structure map. This name should be
        usable as an identifier for the module by machine processing applications such
        as code generation.
            :param title: A short, descriptive, user-friendly title for the structure map.
            :param status: The status of this structure map. Enables tracking the life-cycle of the
        content.
            :param experimental: A Boolean value to indicate that this structure map is authored for testing
        purposes (or education/evaluation/marketing) and is not intended to be used
        for genuine usage.
            :param date: The date  (and optionally time) when the structure map was published. The date
        must change when the business version changes and it must change if the status
        code changes. In addition, it should change when the substantive content of
        the structure map changes.
            :param publisher: The name of the organization or individual that published the structure map.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: A free text natural language description of the structure map from a
        consumer's perspective.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate structure
        map instances.
            :param jurisdiction: A legal or geographic region in which the structure map is intended to be
        used.
            :param purpose: Explanation of why this structure map is needed and why it has been designed
        as it has.
            :param copyright: A copyright statement relating to the structure map and/or its contents.
        Copyright statements are generally legal restrictions on the use and
        publishing of the structure map.
            :param structure: A structure definition used by this map. The structure definition may describe
        instances that are converted, or the instances that are produced.
            :param import_: Other maps used by this map (canonical URLs).
            :param group: Organizes the mapping into manageable chunks for human review/ease of
        maintenance.
        """
        super().__init__(
            resourceType="StructureMap",
            id_=id_,
            meta=meta,
            extension=extension,
            url=url,
            identifier=identifier,
            version=version,
            name=name,
            title=title,
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
            structure=structure,
            import_=import_,
            group=group,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return StructureMapSchema.get_schema(include_extension=include_extension)
