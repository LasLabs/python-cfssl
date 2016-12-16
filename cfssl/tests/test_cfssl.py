# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import mock
import unittest

from ..cfssl import CFSSL, CFSSLRemoteException, requests


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
            'request': 'request',
        }
        self.cfssl.auth_sign(**expect)
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
        expect = {
            'hosts': 'hosts',
            'names': 'names',
            'common_name': 'cn'
        }
        self.cfssl.init_ca(**expect)
        expect['CN'] = 'cn'
        del expect['common_name']
        call.assert_called_once_with(
            'init_ca', 'POST', data=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_new_key(self, call):
        """ It should call with proper args """
        expect = {
            'hosts': 'hosts',
            'names': 'names',
            'common_name': 'cn'
        }
        self.cfssl.new_key(**expect)
        expect['CN'] = 'cn'
        del expect['common_name']
        call.assert_called_once_with(
            'newkey', 'POST', data=expect
        )

    @mock.patch.object(CFSSL, 'call')
    def test_new_cert(self, call):
        """ It should call with proper args """
        expect = {
            'request': 'request',
            'label': 'label',
        }
        self.cfssl.new_cert(**expect)
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
            'host': 'host',
        }
        self.cfssl.scan(**expect)
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
            'certificate_request': 'certificate_request',
        }
        self.cfssl.sign(**expect)
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
