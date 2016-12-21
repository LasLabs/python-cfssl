# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class PolicyAuth(object):
    """ It provides a Certificate Auth policy compatible with CFSSL """

    def __init__(self, name, key, key_type='standard'):
        self.name = name
        self.key = key
        self.key_type = key_type

    def to_api(self):
        """ It returns an object compatible with the API. """
        return {
            'key': self.key,
            'type': self.key_type,
        }
