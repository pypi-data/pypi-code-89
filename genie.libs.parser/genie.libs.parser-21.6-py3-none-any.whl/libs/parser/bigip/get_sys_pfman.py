# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/pfman' resources
# =============================================


class SysPfmanSchema(MetaParser):

    schema = {}


class SysPfman(SysPfmanSchema):
    """ To F5 resource for /mgmt/tm/sys/pfman
    """

    cli_command = "/mgmt/tm/sys/pfman"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
