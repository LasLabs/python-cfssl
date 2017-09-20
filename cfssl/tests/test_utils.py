# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from ..utils import to_api


class TestUtils(unittest.TestCase):
    def test_to_api_native_structure(self):
        """It should return the same object when it doesn't implement to_api.
        """

        expect = "fallback"
        res = to_api(expect)
        self.assertIs(res, expect)

    def test_to_api_object(self):
        """It should delegate to to_api() method of a supported object."""

        class SupportedObject(object):
            def to_api(self):
                return "supported"

        expect = "supported"
        res = to_api(SupportedObject())
        self.assertEqual(res, expect)


if __name__ == '__main__':
    unittest.main()
