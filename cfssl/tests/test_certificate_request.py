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


if __name__ == '__main__':
    unittest.main()
