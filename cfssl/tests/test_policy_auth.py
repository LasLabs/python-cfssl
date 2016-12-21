# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest

from ..models.policy_auth import PolicyAuth


class TestPolicyAuth(unittest.TestCase):

    def setUp(self):
        super(TestPolicyAuth, self).setUp()
        self.vals = {
            'name': 'name',
            'key': 'key',
            'key_type': 'key_type',
        }
        self.model = PolicyAuth(**self.vals)

    def test_to_api(self):
        """ It should return the correctly compatible obj """
        res = self.model.to_api()
        expect = {
            'key': self.vals['key'],
            'type': self.vals['key_type'],
        }
        self.assertDictEqual(res, expect)


if __name__ == '__main__':
    unittest.main()
