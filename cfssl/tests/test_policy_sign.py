# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import mock
import unittest

from datetime import timedelta

from ..models.policy_sign import PolicySign


class TestPolicySign(unittest.TestCase):

    def setUp(self):
        super(TestPolicySign, self).setUp()
        self.vals = {
            'name': 'name',
            'usage_policies': [mock.MagicMock()],
            'auth_policy': mock.MagicMock(),
            'expire_delta': timedelta(seconds=1234),
        }
        self.model = PolicySign(**self.vals)

    def test_to_api(self):
        """ It should return the correctly compatible obj """
        res = self.model.to_api()
        expect = {
            'auth_key': self.vals['auth_policy'].name,
            'expiry': '1234s',
            'usages': [self.vals['usage_policies'][0].to_api()],
        }
        self.assertDictEqual(res, expect)


if __name__ == '__main__':
    unittest.main()
