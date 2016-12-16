# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from setuptools import Command
from unittest import TestLoader, TextTestRunner


class FailTestException(Exception):
    """ It provides a failing build """
    pass


class Tests(Command):
    ''' Run test & coverage, save reports as XML '''

    MODULE_NAMES = [
        'cfssl',
    ]
    user_options = []  # < For Command API compatibility

    def initialize_options(self, ):
        pass

    def finalize_options(self, ):
        pass

    def run(self, ):
        loader = TestLoader()
        tests = loader.discover('.', 'test_*.py')
        t = TextTestRunner(verbosity=1)
        res = t.run(tests)
        if not res.wasSuccessful():
            raise FailTestException()
