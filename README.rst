|License MIT| | |Build Status| | |Coveralls Status| | |Codecov Status| | |Code Climate|

====================
Python CFSSL Library
====================

This library allows you to interact with a remote CFSSL server using Python.

CFSSL is CloudFlare's open source toolkit for everything TLS/SSL. CFSSL is used by
CloudFlare for their internal Certificate Authority infrastructure and for all of
their TLS certificates.

* `Read more on the CloudFlare blog
  <https://blog.cloudflare.com/introducing-cfssl/>`_.
* `View the CFSSL source
  <https://github.com/cloudflare/cfssl>`_.

Installation
============

* Install Python requirements ``pip install -r ./requirements``

Setup
=====

A pre-existing CFSSL server is required to use this library.

Usage
=====

`Read The API Documentation <https://laslabs.github.io/python-cfssl>`_

Known Issues / Road Map
=======================

-  Installation, setup, usage - in ReadMe
-  Add type checking in datamodels

Credits
=======

Images
------

* LasLabs: `Icon <https://repo.laslabs.com/projects/TEM/repos/odoo-module_template/browse/module_name/static/description/icon.svg?raw>`_.

Contributors
------------

* Dave Lasley <dave@laslabs.com>

Maintainer
----------

.. image:: https://laslabs.com/logo.png
   :alt: LasLabs Inc.
   :target: https://laslabs.com

.. |Build Status| image:: https://api.travis-ci.org/LasLabs/python-cfssl.svg?branch=master
   :target: https://travis-ci.org/LasLabs/python-cfssl
.. |Coveralls Status| image:: https://coveralls.io/repos/LasLabs/python-cfssl/badge.svg?branch=master
   :target: https://coveralls.io/r/LasLabs/python-cfssl?branch=master
.. |Codecov Status| image:: https://codecov.io/gh/LasLabs/python-cfssl/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/LasLabs/python-cfssl
.. |Code Climate| image:: https://codeclimate.com/github/laslabs/Python-CFSSL/badges/gpa.svg
   :target: https://codeclimate.com/github/laslabs/Python-CFSSL
.. |License MIT| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: AGPL-3
