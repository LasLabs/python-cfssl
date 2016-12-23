# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from ..defaults import DEFAULT_ALGORITHM, DEFAULT_STRENGTH


class ConfigKey(object):
    """ It provides a Key Config compatible with CFSSL. """

    def __init__(self, algorithm=DEFAULT_ALGORITHM,
                 strength=DEFAULT_STRENGTH):
        """ Initialize a new Client Configuration.

        Args:
            algorithm (str, optional): Algorithm to use for key, one of
                ``rsa`` or ``ecdsa``. Defaults to ``rsa``.
            strength (int, optional): Key bit strength. Defaults to
                ``4096``.
        """
        self.algorithm = algorithm
        self.strength = strength

    def to_api(self):
        """ It returns an object compatible with the API. """
        return {
            'algo': self.algorithm,
            'size': self.strength,
        }
