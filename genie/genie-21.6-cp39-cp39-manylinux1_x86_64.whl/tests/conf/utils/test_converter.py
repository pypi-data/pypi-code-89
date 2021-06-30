#!/usr/bin/env python

# Import unittest module
import os
import unittest

from pyats.topology import loader
from pyats.datastructures import WeakList

# And import what's needed
from genie.conf import Genie
from genie.conf.utils import Converter
from genie.conf.base import Testbed, Device, Link
from genie.conf.base.interface import BaseInterface

class test_converter(unittest.TestCase):
    # TODO : Add more unittest

    def tearDown(self):
        Genie.testbed = None

    def test_init(self):
        '''Convert a pyATS testbed object to Genie testbed objects'''

        test_path = os.path.dirname(os.path.abspath(__file__))
        pyATS_tb = loader.load(os.path.join(test_path, 'tb.yaml'))
        genie_tb = Converter.convert_tb(pyATS_tb)

        # Now let's verify it all worked

        # Verify testbed level
        self.assertEqual(genie_tb.devices.keys(), pyATS_tb.devices.keys())
        self.assertEqual(sorted([link.name for link in genie_tb.links]),
                         sorted([link.name for link in pyATS_tb.links]))

        # Now verify for each device, check interface
        for dev in genie_tb.devices:
            self.assertEqual(genie_tb.devices[dev].interfaces.keys(),
                             pyATS_tb.devices[dev].interfaces.keys())

            # And now verify the links are correct
            for intf in genie_tb.devices[dev].interfaces.keys():
                if genie_tb.devices[dev].interfaces[intf].link:
                    self.assertEqual(
                        genie_tb.devices[dev].interfaces[intf].link.name,
                             pyATS_tb.devices[dev].interfaces[intf].link.name)
                else:
                    # No link, make sure it is the same on both side
                    self.assertEqual(genie_tb.devices[dev].interfaces[intf].links,
                                     WeakList())

                    self.assertEqual(pyATS_tb.devices[dev].interfaces[intf].link,
                                     None)

    def test_interface(self):
        '''Can it figure out the right interface?

        Interface is a bit different, as it needs genie_libs to get the
        right interface'''

        # Get a device to convert
        test_path = os.path.dirname(os.path.abspath(__file__))
        pyATS_tb = loader.load(os.path.join(test_path, 'tb.yaml'))
        tb = Testbed()

        dev1 = pyATS_tb.devices['PE1']

        # Create genie Device object
        device = Device(pyats_device=dev1,
                        name=dev1.name,
                        aliases=[dev1.alias],
                        testbed=tb)

        # set device.os to a type that does exist
        device.os = 'nxos'
        intf = Converter.convert_interface(dev1.interfaces['Ethernet6/45'],
                                           device)
        self.assertTrue(isinstance(intf, BaseInterface))
        self.assertIsNot(type(intf), BaseInterface)


    def test_attributes_unification_between_Pyats_Genie(self):
        '''Testing the inclusion of all the pyats objects attributes in the
           corresponding Genie ones.
        '''

        # Create Genie simple objects
        genie_tb = Testbed(name='my_testbed')
        genie_device = Device(testbed = genie_tb, name='myDevice', os='iosxr')

        # Test pyats objs attributes' addition to the corresponding genie objs
        # --------------------------------------------------------------------
        # Testbed
        test_path = os.path.dirname(os.path.abspath(__file__))
        pyats_tb = loader.load(os.path.join(test_path, 'extensive_tb.yaml'))

        new_genie_tb = Converter.convert_tb(pyats_tb)

        for key in pyats_tb.__dict__.keys():
            self.assertTrue(hasattr(new_genie_tb, key))
            if isinstance(getattr(new_genie_tb, key), dict):
                self.assertEqual(set(getattr(new_genie_tb, key)),
                    set(getattr(pyats_tb, key)))
            else:
                self.assertEqual(getattr(new_genie_tb, key),
                    getattr(pyats_tb, key))

        # Device
        pyats_device = pyats_tb.devices['belfast']
        new_genie_device = Converter.convert_device(pyats_device, new_genie_tb)
        pyats_device.custom.setdefault('abstraction', {})['order'] = ['os']

        for key in pyats_device.__dict__.keys():
            self.assertTrue(hasattr(new_genie_device, key))
            if key == 'connectionmgr' or key == '__testbed__':
                # Objects' Ids won't be the same, so we will compare obj types
                self.assertEqual(type(getattr(new_genie_device, key)),
                    type(getattr(pyats_device, key)))
            elif key == 'connections':
                all(item in getattr(new_genie_device, key).items()
                    for item in getattr(pyats_device, key).items())
            elif isinstance(getattr(new_genie_device, key), dict):
                self.assertEqual(set(getattr(new_genie_device, key)),
                    set(getattr(pyats_device, key)))
            else:
                self.assertEqual(getattr(new_genie_device, key),
                    getattr(pyats_device, key))

        # Interface
        pyats_interface = pyats_device.interfaces['GigabitEthernet0/0/1/17']
        new_genie_interface = Converter.convert_interface(pyats_interface,
            genie_device)

        for key in pyats_interface.__dict__.keys():
            self.assertTrue(hasattr(new_genie_interface, key))
            if key == '__device__':
                # Objects' Ids won't be the same, so we will compare obj types
                self.assertEqual(type(getattr(new_genie_interface, key)),
                    type(getattr(pyats_interface, key)))
            elif isinstance(getattr(new_genie_interface, key), dict):
                self.assertEqual(set(getattr(new_genie_interface, key)),
                    set(getattr(pyats_interface, key)))
            else:
                self.assertEqual(getattr(new_genie_interface, key),
                    getattr(pyats_interface, key))

        # Link
        for lnk in pyats_tb.links:
            pyats_link =  lnk
            break
        new_genie_link = Converter.convert_link(pyats_link, new_genie_tb)

        for key in pyats_link.__dict__.keys():
            self.assertTrue(hasattr(new_genie_link, key))
            if key == 'interfaces':
                continue
            if isinstance(getattr(new_genie_link, key), dict):
                self.assertEqual(set(getattr(new_genie_link, key)),
                    set(getattr(pyats_link, key)))
            else:
                self.assertEqual(getattr(new_genie_link, key),
                    getattr(pyats_link, key))

    def test_callables_unification_between_Pyats_Genie(self):
        '''Testing the inclusion of all the pyats objects attributes in the
           corresponding Genie ones.
        '''

        # Create Genie simple objects
        genie_tb = Testbed(name='my_testbed')
        genie_device = Device(testbed = genie_tb, name='myDevice', os='iosxr')

        # Test pyats objs attributes' addition to the corresponding genie objs
        # --------------------------------------------------------------------
        # Testbed
        test_path = os.path.dirname(os.path.abspath(__file__))
        pyats_tb = loader.load(os.path.join(test_path, 'extensive_tb.yaml'))

        pyats_tb.new_method = lambda: None
        new_genie_tb = Converter.convert_tb(pyats_tb)

        for key in pyats_tb.__dict__.keys():
            self.assertTrue(hasattr(new_genie_tb, key))
            if isinstance(getattr(new_genie_tb, key), dict):
                self.assertEqual(set(getattr(new_genie_tb, key)),
                    set(getattr(pyats_tb, key)))
            else:
                self.assertEqual(getattr(new_genie_tb, key),
                    getattr(pyats_tb, key))

        # Device
        pyats_device = pyats_tb.devices['belfast']
        pyats_tb.device_method = lambda x: x**2
        new_genie_device = Converter.convert_device(pyats_device, new_genie_tb)
        pyats_device.custom.setdefault('abstraction', {})['order'] = ['os']

        for key in pyats_device.__dict__.keys():
            self.assertTrue(hasattr(new_genie_device, key))
            if key == 'connectionmgr' or key == '__testbed__':
                self.assertEqual(type(getattr(new_genie_device, key)),
                    type(getattr(pyats_device, key)))
            elif key == 'connections':
                all(item in getattr(new_genie_device, key).items()
                    for item in getattr(pyats_device, key).items())
            elif isinstance(getattr(new_genie_device, key), dict):
                self.assertEqual(set(getattr(new_genie_device, key)),
                    set(getattr(pyats_device, key)))
            else:
                self.assertEqual(getattr(new_genie_device, key),
                    getattr(pyats_device, key))

        # Interface
        pyats_interface = pyats_device.interfaces['GigabitEthernet0/0/1/17']
        pyats_tb.interface_method = lambda: None
        new_genie_interface = Converter.convert_interface(pyats_interface,
            genie_device)

        for key in pyats_interface.__dict__.keys():
            self.assertTrue(hasattr(new_genie_interface, key))
            if key == '__device__':
                # Objects' Ids won't be the same, so we will compare obj types
                self.assertEqual(type(getattr(new_genie_interface, key)),
                    type(getattr(pyats_interface, key)))
            elif isinstance(getattr(new_genie_interface, key), dict):
                self.assertEqual(set(getattr(new_genie_interface, key)),
                    set(getattr(pyats_interface, key)))
            else:
                self.assertEqual(getattr(new_genie_interface, key),
                    getattr(pyats_interface, key))

        # Link
        for lnk in pyats_tb.links:
            pyats_link = lnk
            break
        pyats_tb.link_method = lambda: None
        new_genie_link = Converter.convert_link(pyats_link, new_genie_tb)

        for key in pyats_link.__dict__.keys():
            self.assertTrue(hasattr(new_genie_link, key))
            if key == 'interfaces':
                continue
            if isinstance(getattr(new_genie_link, key), dict):
                self.assertEqual(set(getattr(new_genie_link, key)),
                    set(getattr(pyats_link, key)))
            else:
                self.assertEqual(getattr(new_genie_link, key),
                    getattr(pyats_link, key))

if __name__ == '__main__':
    unittest.main()
