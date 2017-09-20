# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .host import Host
from .config_key import ConfigKey
from .subject_info import SubjectInfo
from ..utils import to_api


class CertificateRequest(object):
    """ It provides a Certificate Request compatible with CFSSL. """

    def __init__(self, common_name=None, names=None, hosts=None, key=None):
        """ Initialize a new CertificateRequest.

        Args:
            common_name (str, optional): The fully qualified domain name for the
                server. This must be an exact match.
            names (tuple of SubjectInfo, optional):
                Subject Information to be added to the request.
            hosts (tuple of Host, optional): Hosts
                to be added to the request.
            key (ConfigKey, optional): Key configuration
                for the request.
        """
        self.common_name = common_name
        self.names = names or []
        self.hosts = hosts or []
        self.key = key

    def to_api(self):
        """ It returns an object compatible with the API. """
        api = {
            'names': [
                to_api(name) for name in self.names
            ],
            'hosts': [
                to_api(host) for host in self.hosts
            ]
        }
        if self.common_name:
            api['CN'] = self.common_name
        if self.key:
            api['key'] = to_api(self.key)
        return api
