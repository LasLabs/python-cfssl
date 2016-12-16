# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import mock

from ..models.config_client import ConfigClient
from .test_config_mixer import TestConfigMixer

class TestConfigClient(TestConfigMixer):

    def setUp(self):
        super(TestConfigClient, self).setUp()
        self.vals['remotes'] = [mock.MagicMock()]

    @property
    def model(self):
        return ConfigClient(**self.vals)

    def test_to_api(self):
        """ It should return the correctly compatible obj """
        res = self.model.to_api()
        expect = {
            self.vals['remotes'][0].name: self.vals['remotes'][0].to_api()
        }
        self.assertDictEqual(res['remotes'], expect)


if __name__ == '__main__':
    unittest.main()
