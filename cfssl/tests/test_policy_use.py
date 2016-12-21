# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest

from ..models.policy_use import PolicyUse


class TestPolicyUse(unittest.TestCase):

    def setUp(self):
        super(TestPolicyUse, self).setUp()
        self.vals = {
            'name': 'name',
            'code': 'code',
        }
        self.model = PolicyUse(**self.vals)

    def test_to_api(self):
        """ It should return the correctly compatible obj """
        res = self.model.to_api()
        self.assertEqual(res, self.vals['code'])


if __name__ == '__main__':
    unittest.main()
