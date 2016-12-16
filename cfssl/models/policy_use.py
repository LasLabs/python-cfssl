# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class PolicyUse(object):
    """ It provides a Certificate Use policy compatible with CFSSL """

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def to_api(self):
        """ It returns an object compatible with the API. """
        return self.code
