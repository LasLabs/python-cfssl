# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from ..defaults import DEFAULT_EXPIRE_MINUTES


class PolicySign(object):
    """ It provides a Certificate Auth policy compatible with CFSSL """

    def __init__(self, name, usage_policies, auth_policy,
                 expire_minutes=DEFAULT_EXPIRE_MINUTES):
        self.name = name
        self.usage_policies = usage_policies
        self.auth_policy = auth_policy
        self.expire_minutes = expire_minutes

    def to_api(self):
        """ It returns an object compatible with the API. """
        return {
            'auth_key': self.auth_policy.name,
            'expiry': '%dm' % self.expire_minutes,
            'usages': [u.to_api() for u in self.usage_policies],
        }
