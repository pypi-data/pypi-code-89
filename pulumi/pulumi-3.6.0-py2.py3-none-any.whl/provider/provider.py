# Copyright 2016-2021, Pulumi Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional

from pulumi import ResourceOptions, Input, Inputs


class ConstructResult:
    """ConstructResult represents the results of a call to
`Provider.construct`.

    """

    urn: Input[str]
    """The URN of the constructed resource."""

    state: Inputs
    """Any state that was computed during construction."""

    def __init__(self, urn: Input[str], state: Inputs) -> None:
        self.urn = urn
        self.state = state


class Provider:
    """Provider represents an object that implements the resources and
    functions for a particular Pulumi package.

    """

    version: str
    schema: Optional[str]

    def __init__(self, version: str, schema: Optional[str] = None) -> None:
        """
        :param str version: The version of the provider. Must be valid semver.
        :param Optional[str] schema: The JSON-encoded schema for this provider's package.
        """
        self.version = version
        self.schema = schema

    def construct(self, name: str, resource_type: str, inputs: Inputs,
                  options: Optional[ResourceOptions] = None) -> ConstructResult:
        """Construct creates a new component resource.

        :param str name: The name of the resource to create.
        :param str resource_type: The type of the resource to create.
        :param Inputs inputs: The inputs to the resource.
        :param Optional[ResourceOptions] options: The options for the resource.
        """

        raise Exception("Subclass of Provider must implement 'construct'")
