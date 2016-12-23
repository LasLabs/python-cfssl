# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from ..defaults import DEFAULT_EXPIRE_DELTA


class PolicySign(object):
    """ It provides a Certificate Auth policy compatible with CFSSL """

    def __init__(self, name, usage_policies, auth_policy,
                 expire_delta=DEFAULT_EXPIRE_DELTA):
        """ Initialize a new Signing Policy.

        Args:
            name (str): Canonical name for policy.
            usage_policies (tuple of PolicyUser): Usage
                policies that should apply to this signing policy.
            auth_policy (PolicyAuth): Authentication policy that
                should apply to this signing policy.
            expire_delta  (timedelta): Delta representing when
                the signature should expire.
        """
        self.name = name
        self.usage_policies = usage_policies
        self.auth_policy = auth_policy
        self.expire_delta = expire_delta

    def to_api(self):
        """ It returns an object compatible with the API. """
        return {
            'auth_key': self.auth_policy.name,
            'expiry': '%ds' % self.expire_delta.total_seconds(),
            'usages': [u.to_api() for u in self.usage_policies],
        }
