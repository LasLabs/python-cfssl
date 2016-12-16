# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest

from ..models.subject_info import SubjectInfo


class TestSubjectInfo(unittest.TestCase):

    def setUp(self):
        super(TestSubjectInfo, self).setUp()
        self.vals = {
            'org_name': 'org name',
            'org_unit': 'org unit',
            'city': 'city',
            'state': 'state',
            'country': 'country',
        }
        self.model = SubjectInfo(**self.vals)

    def test_to_api(self):
        """ It should return the correctly compatible obj """
        res = self.model.to_api()
        expect = {
            'O': self.vals['org_name'],
            'OU': self.vals['org_unit'],
            'L': self.vals['city'],
            'ST': self.vals['state'],
            'C': self.vals['country'],
        }
        self.assertDictEqual(res, expect)


if __name__ == '__main__':
    unittest.main()
