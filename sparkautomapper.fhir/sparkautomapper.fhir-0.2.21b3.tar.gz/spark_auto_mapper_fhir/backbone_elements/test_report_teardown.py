from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # action (TestReport.Action2)
    from spark_auto_mapper_fhir.backbone_elements.test_report_action2 import (
        TestReportAction2,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestReportTeardown(FhirBackboneElementBase):
    """
    TestReport.Teardown
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        action: FhirList[TestReportAction2],
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param action: The teardown action will only contain an operation.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            action=action,
        )
