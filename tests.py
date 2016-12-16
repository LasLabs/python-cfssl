# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from setuptools import Command

try:
    from xmlrunner import XMLTestRunner
    from unittest import TestLoader
except ImportError:
    pass


class FailTestException(Exception):
    """ It provides a failing build """
    pass


class Tests(Command):
    ''' Run test & coverage, save reports as XML '''

    MODULE_NAMES = [
        'cfssl',
    ]
    TEST_RESULTS = '_results'
    COVERAGE_RESULTS = 'coverage.xml'
    user_options = []  # < For Command API compatibility

    def initialize_options(self, ):
        pass

    def finalize_options(self, ):
        pass

    def run(self, ):
        loader = TestLoader()
        tests = loader.discover('.', 'test_*.py')
        t = XMLTestRunner(verbosity=1, output=self.TEST_RESULTS)
        res = t.run(tests)
        if not res.wasSuccessful():
            raise FailTestException()
