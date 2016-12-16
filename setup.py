# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from setuptools import setup
from setuptools import find_packages
from tests import Tests


setup_vals = {
    'name': 'cfssl',
    'version': '0.0.1',
    'author': 'LasLabs Inc.',
    'author_email': 'support@laslabs.com',
    'description': 'This library will allow you to interact with CFSSL '
                   'using Python.',
    'url': 'https://github.com/laslabs/cfssl-py',
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
}


setup(
    packages=find_packages(exclude=('tests')),
    cmdclass={'test': Tests},
    tests_require=[
        'mock',
    ],
    install_requires=[
        'requests',
    ],
    **setup_vals
)
