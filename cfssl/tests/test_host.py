# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest

from ..models.host import Host


class TestHost(unittest.TestCase):

    def setUp(self):
        super(TestHost, self).setUp()
        self.vals = {
            'name': 'name',
            'host': 'host',
            'port': 443,
        }
        self.model = Host(**self.vals)

    def test_to_api(self):
        """ It should return the correctly compatible obj """
        res = self.model.to_api()
        self.assertEqual(
            res,
            '%s:%s' % (self.vals['host'], self.vals['port']),
        )

    def test_to_api_no_port(self):
        """ It should return the correctly compatible obj """
        del self.vals['port']
        model = Host(**self.vals)
        res = model.to_api()
        self.assertEqual(res, 'host')


if __name__ == '__main__':
    unittest.main()
