# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class PolicyUse(object):
    """ It provides a Certificate Use policy compatible with CFSSL """

    def __init__(self, name, code):
        """ Initialize a new Use Policy.

        Args:
            name (str): Canonical name for policy.
            code (str): CFSSL use code that policy applies to.
        """
        self.name = name
        self.code = code

    def to_api(self):
        """ It returns an object compatible with the API. """
        return self.code
