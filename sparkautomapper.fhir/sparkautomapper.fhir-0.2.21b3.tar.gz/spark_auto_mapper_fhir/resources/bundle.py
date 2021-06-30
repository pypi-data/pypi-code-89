from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.bundle import BundleSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # type_ (BundleType)
    from spark_auto_mapper_fhir.value_sets.bundle_type import BundleTypeCode

    # timestamp (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # total (unsignedInt)
    from spark_auto_mapper_fhir.complex_types.unsigned_int import unsignedInt

    # link (Bundle.Link)
    from spark_auto_mapper_fhir.backbone_elements.bundle_link import BundleLink

    # entry (Bundle.Entry)
    from spark_auto_mapper_fhir.backbone_elements.bundle_entry import BundleEntry

    # signature (Signature)
    from spark_auto_mapper_fhir.complex_types.signature import Signature


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Bundle(FhirResourceBase):
    """
    Bundle
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        type_: BundleTypeCode,
        timestamp: Optional[FhirInstant] = None,
        total: Optional[unsignedInt] = None,
        link: Optional[FhirList[BundleLink]] = None,
        entry: Optional[FhirList[BundleEntry]] = None,
        signature: Optional[Signature] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: A persistent identifier for the bundle that won't change as a bundle is copied
        from server to server.
            :param type_: Indicates the purpose of this bundle - how it is intended to be used.
            :param timestamp: The date/time that the bundle was assembled - i.e. when the resources were
        placed in the bundle.
            :param total: If a set of search matches, this is the total number of entries of type
        'match' across all pages in the search.  It does not include search.mode =
        'include' or 'outcome' entries and it does not provide a count of the number
        of entries in the Bundle.
            :param link: A series of links that provide context to this bundle.
            :param entry: An entry in a bundle resource - will either contain a resource or information
        about a resource (transactions and history only).
            :param signature: Digital Signature - base64 encoded. XML-DSig or a JWT.
        """
        super().__init__(
            resourceType="Bundle",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            type_=type_,
            timestamp=timestamp,
            total=total,
            link=link,
            entry=entry,
            signature=signature,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return BundleSchema.get_schema(include_extension=include_extension)
