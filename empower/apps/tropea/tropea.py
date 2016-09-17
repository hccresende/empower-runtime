#!/usr/bin/env python3
#
# Copyright (c) 2016 Roberto Riggio, Tejas
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

"""EmPOWER application implementing an LVNF Chaining."""

from empower.core.app import EmpowerApp
from empower.core.app import DEFAULT_PERIOD


class Tropea(EmpowerApp):
    pass


def launch(tenant_id, every=DEFAULT_PERIOD):
    """ Initialize the module. """

    return Tropea(tenant_id=tenant_id, every=every)