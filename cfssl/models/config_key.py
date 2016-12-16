# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from ..defaults import DEFAULT_ALGORITHM, DEFAULT_STRENGTH


class ConfigKey(object):
    """ It provides a Key Config compatible with CFSSL. """

    def __init__(self, algorithm=DEFAULT_ALGORITHM,
                 strength=DEFAULT_STRENGTH):
        self.algorithm = algorithm
        self.strength = strength

    def to_api(self):
        """ It returns an object compatible with the API. """
        return {
            'algo': self.algorithm,
            'size': self.strength,
        }
