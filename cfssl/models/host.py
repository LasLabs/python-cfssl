# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class Host(object):
    """ It provides a Host compatible with CFSSL. """

    def __init__(self, name, host, port=None):
        self.name = name
        self.host = host
        self.port = port

    def to_api(self):
        """ It returns an object compatible with the API. """
        if self.port:
            return '%s:%d' % (self.host, self.port)
        return self.host
