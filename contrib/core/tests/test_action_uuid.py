#!/usr/bin/env python

# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from st2tests.base import BaseActionTestCase

from generate_uuid import GenerateUUID


class GenerateUUIDActionTestCase(BaseActionTestCase):
    action_cls = GenerateUUID

    def test_run(self):
        action = self.get_action_instance()

        # accepts uuid1 as a type
        result = action.run(uuid_type='uuid1')
        self.assertTrue(result)

        # accepts uuid4 as a type
        result = action.run(uuid_type='uuid4')
        self.assertTrue(result)

        # fails on incorrect type
        result = action.run(uuid_type='foobar')
        self.assertFalse(result)
