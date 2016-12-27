# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import logging
import mock
import unittest

from ..cfssl import (CFSSL,
                     CFSSLRemoteException,
                     requests,
                     )

_logger = logging.getLogger(__name__)

try:
    from cfssl import CertificateRequest
except ImportError:
    _logger.info('CFSSL Python library not installed.')


class TestCFSSL(unittest.TestCase):

    def setUp(self):
        super(TestCFSSL, self).setUp()
        self.cfssl = CFSSL('test', 1)

    def test_uri_base_https(self):
        """ It should have an HTTP URI by default """
        self.assertIn('https://', self.cfssl.uri_base)

    def test_uri_base_http(self):
        """ It should have an HTTP URI if someone decides to be crazy """
        cfssl = CFSSL('test', 1, False)
        self.assertIn('http://', cfssl.uri_base)

    @mock.patch.object(CFSSL, 'call')
    def test_auth_sign(self, call):
        """ It should call with proper args """
        expect = {
            'token': 'token',
            'request': mock.MagicMock(),
        }
        self.cfssl.auth_sign(**expect)
        expect['request'] = expect['request'].to_api()
        call.assert_called_once_with(
            'authsign', 'POST', data=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_bundle(self, call):
        """ It should call with proper args """
        expect = {
            'certificate': 'certificate',
            'flavor': 'flavor',
        }
        self.cfssl.bundle(**expect)
        call.assert_called_once_with(
            'bundle', 'POST', data=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_info(self, call):
        """ It should call with proper args """
        expect = {
            'label': 'label',
        }
        self.cfssl.info(**expect)
        call.assert_called_once_with(
            'info', 'POST', data=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_init_ca(self, call):
        """ It should call with proper args """
        csr_vals = {
            'hosts': [mock.MagicMock()],
            'names': [mock.MagicMock()],
            'common_name': 'cn',
            'key': mock.MagicMock(),
        }
        csr = CertificateRequest(**csr_vals)
        expect = {'ca': mock.MagicMock(),
                  'certificate_request': csr}
        self.cfssl.init_ca(**expect)
        expect.update(csr_vals)
        expect['CN'] = 'cn'
        del expect['common_name']
        del expect['certificate_request']
        expect['hosts'][0]= expect['hosts'][0].to_api()
        expect['names'][0] = expect['names'][0].to_api()
        expect['key'] = expect['key'].to_api()
        expect['ca'] = expect['ca'].to_api()
        call.assert_called_once_with(
            'init_ca', 'POST', data=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_new_key(self, call):
        """ It should call with proper args """
        expect = {
            'hosts': [mock.MagicMock()],
            'names': [mock.MagicMock()],
            'common_name': 'cn',
            'ca': mock.MagicMock(),
            'key': mock.MagicMock(),
        }
        self.cfssl.new_key(**expect)
        expect['CN'] = 'cn'
        del expect['common_name']
        expect['hosts'][0]= expect['hosts'][0].to_api()
        expect['names'][0] = expect['names'][0].to_api()
        expect['ca'] = expect['ca'].to_api()
        expect['key'] = expect['key'].to_api()
        call.assert_called_once_with(
            'newkey', 'POST', data=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_new_cert(self, call):
        """ It should call with proper args """
        expect = {
            'request': mock.MagicMock(),
            'label': 'label',
        }
        self.cfssl.new_cert(**expect)
        expect['request'] = expect['request'].to_api()
        call.assert_called_once_with(
            'newcert', 'POST', data=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_revoke(self, call):
        """ It should call with proper args """
        expect = {
            'serial': 'Ben-S',
            'authority_key_id': 'REVOKE!',
            'reason': 'The derphead lost it',
        }
        self.cfssl.revoke(**expect)
        call.assert_called_once_with(
            'revoke', 'POST', data=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_scan(self, call):
        """ It should call with proper args """
        expect = {
            'host': mock.MagicMock(),
        }
        self.cfssl.scan(**expect)
        expect['host'] = expect['host'].to_api()
        call.assert_called_once_with(
            'scan', params=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_scan_info(self, call):
        """ It should call with proper args """
        self.cfssl.scan_info()
        call.assert_called_once_with('scaninfo')

    @mock.patch.object(CFSSL, 'call')
    def test_sign(self, call):
        """ It should call with proper args """
        expect = {
            'certificate_request': mock.MagicMock(),
            'hosts': [mock.MagicMock()],
            'profile': mock.MagicMock(),
        }
        self.cfssl.sign(**expect)
        expect['certificate_request'] = expect['certificate_request'].to_api()
        expect['hosts'][0] = expect['hosts'][0].to_api()
        expect['profile'] = expect['profile'].to_api()
        call.assert_called_once_with(
            'sign', 'POST', data=expect
        )

    @mock.patch.object(requests, 'request')
    def test_call_request(self, requests):
        """ It should call requests with proper args """
        self.cfssl.call('endpoint', 'method', 'params', 'data')
        requests.assert_called_once_with(
            method='method',
            url='https://test:1/api/v1/cfssl/endpoint',
            params='params',
            data='data',
            verify=True,
        )

    @mock.patch.object(requests, 'request')
    def test_call_error(self, requests):
        """ It should raise on non-success response """
        requests().json.return_value = {'success': False}
        with self.assertRaises(CFSSLRemoteException):
            self.cfssl.call('None')

    @mock.patch.object(requests, 'request')
    def test_call_success(self, requests):
        """ It should reteurn result on success response """
        requests().json.return_value = {'success': True,
                                        'result': 'result'}
        res = self.cfssl.call(None)
        self.assertEqual(res, 'result')

if __name__ == '__main__':
    unittest.main()
