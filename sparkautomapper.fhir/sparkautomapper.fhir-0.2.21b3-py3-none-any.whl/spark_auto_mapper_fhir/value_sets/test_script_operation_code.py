from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestScriptOperationCodeCode(FhirValueSetBase):
    """
    TestScriptOperationCode
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/testscript-operation-codes
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/testscript-operation-codes"


class TestScriptOperationCodeCodeValues:
    """
    Read the current state of the resource.
    """

    Read = TestScriptOperationCodeCode("read")
    """
    Read the state of a specific version of the resource.
    """
    VersionRead = TestScriptOperationCodeCode("vread")
    """
    Update an existing resource by its id.
    """
    Update = TestScriptOperationCodeCode("update")
    """
    Update an existing resource by its id (or create it if it is new).
    """
    CreateUsingUpdate = TestScriptOperationCodeCode("updateCreate")
    """
    Patch an existing resource by its id.
    """
    Patch = TestScriptOperationCodeCode("patch")
    """
    Delete a resource.
    """
    Delete = TestScriptOperationCodeCode("delete")
    """
    Conditionally delete a single resource based on search parameters.
    """
    ConditionalDeleteSingle = TestScriptOperationCodeCode("deleteCondSingle")
    """
    Conditionally delete one or more resources based on search parameters.
    """
    ConditionalDeleteMultiple = TestScriptOperationCodeCode("deleteCondMultiple")
    """
    Retrieve the change history for a particular resource or resource type.
    """
    History = TestScriptOperationCodeCode("history")
    """
    Create a new resource with a server assigned id.
    """
    Create = TestScriptOperationCodeCode("create")
    """
    Search based on some filter criteria.
    """
    Search = TestScriptOperationCodeCode("search")
    """
    Update, create or delete a set of resources as independent actions.
    """
    Batch = TestScriptOperationCodeCode("batch")
    """
    Update, create or delete a set of resources as a single transaction.
    """
    Transaction = TestScriptOperationCodeCode("transaction")
    """
    Get a capability statement for the system.
    """
    Capabilities = TestScriptOperationCodeCode("capabilities")
    """
    Realizes an ActivityDefinition in a specific context
    """
    _apply = TestScriptOperationCodeCode("apply")
    """
    Closure Table Maintenance
    """
    _closure = TestScriptOperationCodeCode("closure")
    """
    Finding Codes based on supplied properties
    """
    _find_matches = TestScriptOperationCodeCode("find-matches")
    """
    Compare two systems CapabilityStatements
    """
    _conforms = TestScriptOperationCodeCode("conforms")
    """
    Aggregates and returns the parameters and data requirements for a resource and all its dependencies as a single module definition
    """
    _data_requirements = TestScriptOperationCodeCode("data-requirements")
    """
    Generate a Document
    """
    _document = TestScriptOperationCodeCode("document")
    """
    Request clinical decision support guidance based on a specific decision support module
    """
    _evaluate = TestScriptOperationCodeCode("evaluate")
    """
    Invoke an eMeasure and obtain the results
    """
    _evaluate_measure = TestScriptOperationCodeCode("evaluate-measure")
    """
    Return all the related information as described in the Encounter or Patient
    """
    _everything = TestScriptOperationCodeCode("everything")
    """
    Value Set Expansion
    """
    _expand = TestScriptOperationCodeCode("expand")
    """
    Find a functional list
    """
    _find = TestScriptOperationCodeCode("find")
    """
    Invoke a GraphQL query
    """
    _graphql = TestScriptOperationCodeCode("graphql")
    """
    Test if a server implements a client's required operations
    """
    _implements = TestScriptOperationCodeCode("implements")
    """
    Last N Observations Query
    """
    _lastn = TestScriptOperationCodeCode("lastn")
    """
    Concept Look Up and Decomposition
    """
    _lookup = TestScriptOperationCodeCode("lookup")
    """
    Find patient matches using MPI based logic
    """
    _match = TestScriptOperationCodeCode("match")
    """
    Access a list of profiles, tags, and security labels
    """
    _meta = TestScriptOperationCodeCode("meta")
    """
    Add profiles, tags, and security labels to a resource
    """
    _meta_add = TestScriptOperationCodeCode("meta-add")
    """
    Delete profiles, tags, and security labels for a resource
    """
    _meta_delete = TestScriptOperationCodeCode("meta-delete")
    """
    Populate Questionnaire
    """
    _populate = TestScriptOperationCodeCode("populate")
    """
    Generate HTML for Questionnaire
    """
    _populatehtml = TestScriptOperationCodeCode("populatehtml")
    """
    Generate a link to a Questionnaire completion webpage
    """
    _populatelink = TestScriptOperationCodeCode("populatelink")
    """
    Process a message according to the defined event
    """
    _process_message = TestScriptOperationCodeCode("process-message")
    """
    Build Questionnaire
    """
    _questionnaire = TestScriptOperationCodeCode("questionnaire")
    """
    Observation Statistics
    """
    _stats = TestScriptOperationCodeCode("stats")
    """
    Fetch a subset of the CapabilityStatement resource
    """
    _subset = TestScriptOperationCodeCode("subset")
    """
    CodeSystem Subsumption Testing
    """
    _subsumes = TestScriptOperationCodeCode("subsumes")
    """
    Model Instance Transformation
    """
    _transform = TestScriptOperationCodeCode("transform")
    """
    Concept Translation
    """
    _translate = TestScriptOperationCodeCode("translate")
    """
    Validate a resource
    """
    _validate = TestScriptOperationCodeCode("validate")
    """
    ValueSet based Validation
    """
    _validate_code = TestScriptOperationCodeCode("validate-code")
