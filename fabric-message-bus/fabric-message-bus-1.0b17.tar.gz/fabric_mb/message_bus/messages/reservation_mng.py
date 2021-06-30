#!/usr/bin/env python3
# MIT License
#
# Copyright (c) 2020 FABRIC Testbed
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#
# Author: Komal Thareja (kthare10@renci.org)
"""
Represents Reservation object returned from Management Interface APIs
"""
import pickle
from fabric_mb.message_bus.message_bus_exception import MessageBusException


class ReservationMng:
    """
    Implements Avro representation of a Reservation returned from Management Interface
    """
    def __init__(self):
        self.name = self.__class__.__name__
        self.reservation_id = None
        self.slice_id = None
        self.start = None
        self.end = None
        self.requested_end = None
        self.rtype = None
        self.units = None
        self.state = None
        self.pending_state = None
        self.local = None
        self.config = None
        self.request = None
        self.resource = None
        self.notices = None
        self.sliver = None

    def from_dict(self, value: dict):
        """
        The Avro Python library does not support code generation.
        For this reason we must provide conversion from dict to our class for de-serialization
        :param value: incoming message dictionary
        """
        self.name = value.get('name', None)
        self.reservation_id = value.get('reservation_id', None)
        self.slice_id = value.get('slice_id', None)
        self.start = value.get('start', None)
        self.end = value.get('end', None)
        self.requested_end = value.get('requested_end', None)
        self.rtype = value.get('rtype', None)
        self.units = value.get('units', None)
        self.state = value.get('state', None)
        self.pending_state = value.get('pending_state', None)
        self.local = value.get('local', None)
        self.config = value.get('config', None)
        self.request = value.get('request', None)
        self.resource = value.get('resource', None)
        self.notices = value.get('notices', None)
        self.sliver = value.get('sliver', None)

    def to_dict(self) -> dict:
        """
        The Avro Python library does not support code generation.
        For this reason we must provide a dict representation of our class for serialization.
        :return dict representing the class
        """
        if not self.validate():
            raise MessageBusException("Invalid arguments")

        result = {'name': self.name,
                  'reservation_id': self.reservation_id,
                  'rtype': self.rtype,
                  'notices': self.notices}
        if self.slice_id is not None:
            result['slice_id'] = self.slice_id

        if self.start is not None:
            result['start'] = self.start

        if self.end is not None:
            result['end'] = self.end

        if self.requested_end is not None:
            result['requested_end'] = self.requested_end

        if self.units is not None:
            result['units'] = self.units

        if self.state is not None:
            result['state'] = self.state

        if self.pending_state is not None:
            result['pending_state'] = self.pending_state

        if self.local is not None:
            result['local'] = self.local

        if self.config is not None:
            result['config'] = self.config

        if self.request is not None:
            result['request'] = self.request

        if self.resource is not None:
            result['resource'] = self.resource

        if self.sliver is not None:
            result['sliver'] = self.sliver

        return result

    @staticmethod
    def sliver_to_bytes(sliver):
        if sliver is not None:
            return pickle.dumps(sliver)
        return None

    @staticmethod
    def bytes_to_sliver(sliver_bytes):
        if sliver_bytes is not None:
            return pickle.loads(sliver_bytes)
        return sliver_bytes

    def print(self):
        """
        Prints ReservationMng
        """
        print("")
        print(f"Reservation ID: {self.reservation_id} Slice ID: {self.slice_id}")
        if self.rtype is not None or self.notices is not None:
            print(f"Resource Type: {self.rtype} Notices: {self.notices}")

        if self.start is not None or self.end is not None or self.requested_end is not None:
            print(f"Start: {self.start} End: {self.end} Requested End: {self.requested_end}")

        if self.units is not None or self.state is not None or self.pending_state is not None:
            print(f"Units: {self.units} State: {self.state} Pending State: {self.pending_state}")

        if self.local is not None:
            print(f"Local Properties: {self.local}")
        if self.config is not None:
            print(f"Config Properties: {self.config}")
        if self.request is not None:
            print(f"Request Properties: {self.request}")
        if self.resource is not None:
            print(f"Resource Properties: {self.resource}")

        print("")

    def __str__(self):
        return f"name: {self.name} reservation_id: {self.reservation_id} slice_id: {self.slice_id} start: " \
               f"{self.start} end: {self.end} requested_end: {self.requested_end} rtype: {self.rtype} " \
               f"units: {self.units} state: {self.state} pending_state: {self.pending_state} local: {self.local}" \
               f" config: {self.config} request: {self.request} resource: {self.resource} notices: {self.notices} " \
               f"sliver: {self.sliver}"

    def get_reservation_id(self) -> str:
        """
        Returns Reservation ID
        @return reservation id
        """
        return self.reservation_id

    def set_reservation_id(self, value: str):
        """
        Set reservation id
        @param value value
        """
        self.reservation_id = value

    def get_slice_id(self) -> str:
        """
        Return Slice Id
        @return slice id
        """
        return self.slice_id

    def set_slice_id(self, value: str):
        """
        Set slice id
        @param value value
        """
        self.slice_id = value

    def get_start(self) -> int:
        """
        Return Start Lease Time
        @return start time
        """
        return self.start

    def set_start(self, value: int):
        """
        Set Start lease time
        @param value value
        """
        self.start = value

    def get_end(self) -> int:
        """
        Return End lease time
        @return end time
        """
        return self.end

    def set_end(self, value: int):
        """
        Set end lease time
        @param value value
        """
        self.end = value

    def get_requested_end(self) -> int:
        """
        Return requested end lease time
        @return requested end lease time
        """
        return self.requested_end

    def set_requested_end(self, value: int):
        """
        Set requested lease end time
        @param value value
        """
        self.requested_end = value

    def get_resource_type(self) -> str:
        """
        Return resource type
        @return resource type
        """
        return self.rtype

    def set_resource_type(self, value: str):
        """
        Set resource type
        @param value value
        """
        self.rtype = value

    def get_units(self) -> int:
        """
        Return Units
        @param return unitds
        """
        return self.units

    def set_units(self, value: int):
        """
        Set units
        @param value value
        """
        self.units = value

    def get_state(self) -> int:
        """
        Return reservation state
        @return reservation state
        """
        return self.state

    def set_state(self, value: int):
        """
        Set reservation state
        @param value value
        """
        self.state = value

    def get_pending_state(self) -> int:
        """
        Return Pending State
        @return pending state
        """
        return self.pending_state

    def set_pending_state(self, value: int):
        """
        Set pending state
        @param value value
        """
        self.pending_state = value

    def get_local_properties(self) -> dict:
        """
        Return local properties
        @return local properties
        """
        return self.local

    def set_local_properties(self, value: dict):
        """
        Set local properties
        @param value value
        """
        self.local = value

    def get_config_properties(self) -> dict:
        """
        Return config properties
        @return config properties
        """
        return self.config

    def set_config_properties(self, value: dict):
        """
        Set config properties
        @param value value
        """
        self.config = value

    def get_request_properties(self) -> dict:
        """
        Return request properties
        @return request properties
        """
        return self.request

    def set_request_properties(self, value: dict):
        """
        Set request properties
        @param value value
        """
        self.request = value

    def get_resource_properties(self) -> dict:
        """
        Return resource properties
        @return resource properties
        """
        return self.resource

    def set_resource_properties(self, value: dict):
        """
        Set resource properties
        @param value value
        """
        self.resource = value

    def get_notices(self) -> str:
        """
        Return notices
        @return notices
        """
        return self.notices

    def set_notices(self, value: str):
        """
        Set notices
        @param value value
        """
        self.notices = value

    def get_sliver(self):
        return self.bytes_to_sliver(self.sliver)

    def set_sliver(self, sliver):
        self.sliver = self.sliver_to_bytes(sliver)

    def __eq__(self, other):
        if not isinstance(other, ReservationMng):
            return False

        return self.name == other.name and self.reservation_id == other.reservation_id and \
            self.slice_id == other.slice_id and self.start == other.start and self.end == other.end and \
            self.requested_end == other.requested_end and self.rtype == other.rtype and self.units == other.units and \
            self.state == other.state and self.pending_state == other.pending_state and self.local == other.local and \
            self.request == other.request and self.resource == other.resource and self.notices == other.notices and \
            self.sliver == other.sliver

    def validate(self) -> bool:
        """
        Check if the object is valid and contains all mandatory fields
        :return True on success; False on failure
        """
        ret_val = True
        if self.reservation_id is None or self.rtype is None or self.notices is None:
            ret_val = False
        return ret_val
