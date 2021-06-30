import os

from ruamel import yaml

import great_expectations as ge
from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest

# Google BigQuery config
# TODO : configure additional environment variables for Azure pipeline to perform full integration tests on bigquery data.
gcp_project = os.environ.get("GCP_PROJECT")
bigquery_dataset = os.environ.get("GCP_BIGQUERY_DATASET")

CONNECTION_STRING = f"bigquery://{gcp_project}/{bigquery_dataset}"

# This utility is not for general use. It is only to support testing.
from util import load_data_into_database

load_data_into_database(
    table_name="taxi_data",
    csv_path="./data/yellow_trip_data_sample_2019-01.csv",
    connection_string=CONNECTION_STRING,
)

context = ge.get_context()

datasource_config = {
    "name": "my_bigquery_datasource",
    "class_name": "Datasource",
    "execution_engine": {
        "class_name": "SqlAlchemyExecutionEngine",
        "connection_string": "bigquery://<GCP_PROJECT_NAME>/<BIGQUERY_DATASET>",
    },
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "batch_identifiers": ["default_identifier_name"],
        },
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetSqlDataConnector",
            "name": "whole_table",
        },
    },
}
# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the yaml above.
datasource_config["execution_engine"]["connection_string"] = CONNECTION_STRING

context.test_yaml_config(yaml.dump(datasource_config))

context.add_datasource(**datasource_config)

# Test for RuntimeBatchRequest using a query. bigquery_temp_table name is passed in as batch_spec_passthrough
batch_request = RuntimeBatchRequest(
    datasource_name="my_bigquery_datasource",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="default_name",  # this can be anything that identifies this data
    runtime_parameters={"query": "SELECT * from demo.taxi_data LIMIT 10"},
    batch_identifiers={"default_identifier_name": "something_something"},
    batch_spec_passthrough={
        "bigquery_temp_table": "ge_temp"
    },  # this is the name of the table you would like to use a 'temp_table'
)

context.create_expectation_suite(
    expectation_suite_name="test_suite", overwrite_existing=True
)
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="test_suite"
)
print(validator.head())

# NOTE: The following code is only for testing and can be ignored by users.
assert isinstance(validator, ge.validator.validator.Validator)

# Test for BatchRequest naming a table. bigquery_temp_table name is passed in as batch_spec_passthrough
batch_request = BatchRequest(
    datasource_name="my_bigquery_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="taxi_data",  # this is the name of the table you want to retrieve
    batch_spec_passthrough={
        "bigquery_temp_table": "ge_temp"
    },  # this is the name of the table you would like to use a 'temp_table'
)
context.create_expectation_suite(
    expectation_suite_name="test_suite", overwrite_existing=True
)
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="test_suite"
)
print(validator.head())

# NOTE: The following code is only for testing and can be ignored by users.
assert isinstance(validator, ge.validator.validator.Validator)
assert [ds["name"] for ds in context.list_datasources()] == ["my_bigquery_datasource"]
assert "taxi_data" in set(
    context.get_available_data_asset_names()["my_bigquery_datasource"][
        "default_inferred_data_connector_name"
    ]
)
