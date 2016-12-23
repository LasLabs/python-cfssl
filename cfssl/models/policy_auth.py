# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class PolicyAuth(object):
    """ It provides a Certificate Auth policy compatible with CFSSL """

    def __init__(self, name, key, key_type='standard'):
        """ Initialize a new Authentication Policy.

        Args:
            name (str): Canonical name for policy.
            key (str): Key/password data.
            key_type (str): Type of key. Currently only ``standard`` is
                supported.
        """
        self.name = name
        self.key = key
        self.key_type = key_type

    def to_api(self):
        """ It returns an object compatible with the API. """
        return {
            'key': self.key,
            'type': self.key_type,
        }
