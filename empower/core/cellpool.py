#!/usr/bin/env python3
#
# Copyright (c) 2016 Roberto Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

"""EmPOWER resouce pool and resource block classes."""


class CellPool(list):
    """EmPOWER cell pool.

    This extends the list in order to add a few filtering and sorting methods
    """

    def sort_by_rsrp(self, addr):
        """Return list sorted by rsrp for the specified address."""

        cells = sorted(self, key=lambda x: x.rrc_measurements[addr]['mov_rssi'],
                       reverse=True)

        return CellPool(cells)

    def first(self):
        """Return first entry in the list."""

        cell = list.__getitem__(self, 0)
        return CellPool([cell])

    def last(self):
        """Return last entry in the list."""

        cell = list.__getitem__(self, -1)
        return CellPool([cell])


class Cell:
    """An eNB cell."""

    def __init__(self, vbs, pci, cap, dl_earfcn, dl_prbs, ul_earfcn, ul_prbs):
        self.vbs = vbs
        self.pci = pci
        self.cap = cap
        self.rrc_measurements = {}
        self.mac_reports = {}
        self.dl_earfcn = dl_earfcn
        self.dl_prbs = dl_prbs
        self.ul_earfcn = ul_earfcn
        self.ul_prbs = ul_prbs

    def __repr__(self):
        """Return string representation."""

        return "vbs %s pci %u dl_earfcn %u dl_earfcn %u" % \
            (self.vbs.addr, self.pci, self.dl_earfcn, self.ul_earfcn)

    def __hash__(self):
        return hash(self.vbs) + hash(self.pci)

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.vbs == other.vbs and self.pci == other.pci
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def to_dict(self):
        """Return a JSON-serializable dictionary representing the CPP."""

        out = {}

        out['addr'] = self.vbs.addr
        out['pci'] = self.pci
        out['cap'] = self.cap
        out['dl_earfcn'] = self.dl_earfcn
        out['dl_prbs'] = self.dl_prbs
        out['ul_earfcn'] = self.ul_earfcn
        out['ul_prbs'] = self.ul_prbs
        out['mac_reports'] = self.mac_reports

        return out