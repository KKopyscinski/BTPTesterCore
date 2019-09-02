#
# Copyright (c) 2019 JUUL Labs, Inc.
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
#

import logging
import unittest

from projects.android.iutctl import AndroidCtl
from projects.mynewt.iutctl import MynewtCtl
from testcases.GattTestCase import GattTestCase
from testcases.GapTestCase import GapTestCase


def main():
    print("Starting tester")
    format = ("%(asctime)s %(name)-20s %(levelname)s %(threadName)-20s "
              "%(filename)-25s %(lineno)-5s %(funcName)-25s : %(message)s")
    logging.basicConfig(level=logging.DEBUG,
                        format=format)
    logger = logging.getLogger('websockets.server')
    logger.setLevel(logging.ERROR)
    logger.addHandler(logging.StreamHandler())

    mynewt1 = MynewtCtl('/dev/ttyACM0', '683802616')
    mynewt2 = MynewtCtl('/dev/ttyACM1', '683414473')
    # android = AndroidCtl('192.168.9.123', 8765)

    def suite():
        suite = unittest.TestSuite()
        # suite.addTest(GattTestCase('test_gattc_find_incl_svcs',
        #                            mynewt1, mynewt2))
        suite.addTests(GapTestCase.init_testcases(mynewt1, mynewt2))
        suite.addTests(GattTestCase.init_testcases(mynewt1, mynewt2))
        return suite

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())


if __name__ == "__main__":
    main()
