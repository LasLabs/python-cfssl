# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest

from ..models.config_key import ConfigKey


class TestConfigKey(unittest.TestCase):

    def setUp(self):
        super(TestConfigKey, self).setUp()
        self.vals = {
            'algorithm': 'rsa',
            'strength': 2048,
        }
        self.model = ConfigKey(**self.vals)

    def test_to_api(self):
        """ It should return the correctly compatible obj """
        res = self.model.to_api()
        expect = {
            'algo': self.vals['algorithm'],
            'size': self.vals['strength'],
        }
        self.assertDictEqual(res, expect)


if __name__ == '__main__':
    unittest.main()
