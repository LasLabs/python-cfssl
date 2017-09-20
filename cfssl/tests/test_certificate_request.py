# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import mock
import unittest

from ..models.certificate_request import CertificateRequest


class TestCertificateRequest(unittest.TestCase):

    def setUp(self):
        super(TestCertificateRequest, self).setUp()
        self.vals = {
            'common_name': 'common_name',
            'names': [mock.MagicMock()],
            'hosts': [mock.MagicMock()],
            'key': mock.MagicMock(),
        }
        self.model = CertificateRequest(**self.vals)

        self.partial_vals = {
            'names': [mock.MagicMock()],
            'hosts': [mock.MagicMock()],
        }
        self.model_partial = CertificateRequest(**self.partial_vals)

    def test_to_api(self):
        """ It should return the correctly compatible obj """
        res = self.model.to_api()
        expect = {
            'CN': self.vals['common_name'],
            'names': [self.vals['names'][0].to_api()],
            'hosts': [self.vals['hosts'][0].to_api()],
            'key': self.vals['key'].to_api(),
        }
        self.assertDictEqual(res, expect)

    def test_to_api_partial(self):
        """It should handle when no CN and no key are defined"""
        res = self.model_partial.to_api()
        expect = {
            'names': [self.partial_vals['names'][0].to_api()],
            'hosts': [self.partial_vals['hosts'][0].to_api()],
        }
        self.assertDictEqual(res, expect)


if __name__ == '__main__':
    unittest.main()
