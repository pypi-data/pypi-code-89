from genie import abstract
abstract.declare_token(__name__)

from .. import Ospf as BaseOspf

class Ospf(BaseOspf):
    def abc(self):
        print(self, 'in nxos')
    pass
