# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import mock
import unittest

from ..models.config_mixer import ConfigMixer


class TestConfigMixer(unittest.TestCase):

    def setUp(self):
        super(TestConfigMixer, self).setUp()
        self.vals = {
            'sign_policy_default': mock.MagicMock(),
            'sign_policies_add': [mock.MagicMock()],
            'auth_policies': [mock.MagicMock()],
        }

    @property
    def model(self):
        return ConfigMixer(**self.vals)

    def test_to_api(self):
        """ It should return the correctly compatible obj """
        res = self.model.to_api()
        sign_policy = self.vals['sign_policies_add'][0]
        auth_policy = self.vals['auth_policies'][0]
        expect = {
            'signing': {
                'default': self.vals['sign_policy_default'].to_api(),
                'profiles': {
                    sign_policy.name: sign_policy.to_api(),
                },
            },
            'auth_keys': {
                auth_policy.name: auth_policy.to_api(),
            },
        }
        self.assertDictEqual(res, expect)


if __name__ == '__main__':
    unittest.main()
