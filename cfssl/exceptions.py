# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import requests


class CFSSLException(EnvironmentError):
    """ This exception is raised from errors in the CFSSL Library. """


class CFSSLRemoteException(CFSSLException):
    """ This exception is raised to indicate issues returned from API. """
