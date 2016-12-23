# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class Host(object):
    """ It provides a Host compatible with CFSSL. """

    def __init__(self, name, host, port=None):
        """ Initialize a new Client Configuration.

        Args:
            name (str): Canonical name of host/remote.
            host (str): Advertised host name or IP for host.
            port (int, optional): Port number advertised by host, if
                any.
        """
        self.name = name
        self.host = host
        self.port = port

    def to_api(self):
        """ It returns an object compatible with the API. """
        if self.port:
            return '%s:%d' % (self.host, self.port)
        return self.host
