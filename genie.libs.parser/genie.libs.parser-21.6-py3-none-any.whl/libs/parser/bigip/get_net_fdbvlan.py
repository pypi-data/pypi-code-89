# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/fdb/vlan' resources
# =============================================


class NetFdbVlanSchema(MetaParser):

    schema = {}


class NetFdbVlan(NetFdbVlanSchema):
    """ To F5 resource for /mgmt/tm/net/fdb/vlan
    """

    cli_command = "/mgmt/tm/net/fdb/vlan"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
