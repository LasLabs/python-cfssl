# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class ConfigMixer(object):
    """ It provides a mixer for the Client and Server Configs """

    def __init__(self, sign_policy_default, sign_policies_add, auth_policies):
        """ Initialize a new General Configuration for Server or Client.

        Args:
            sign_policy_default (PolicySign): Default signing
                policy for entity to use.
            sign_policies_add (tuple of PolicySign):
                Additional signing policies to use for the entity.
            auth_policies (tuple of PolicyAuth): Auth
                policies for the entity.
        """
        self.sign_policy = sign_policy_default
        self.sign_policies = sign_policies_add
        self.auth_policies = auth_policies

    def to_api(self):
        """ It returns an object compatible with the API. """
        return {
            'signing': {
                'default': self.sign_policy.to_api(),
                'profiles': {
                    p.name: p.to_api() for p in self.sign_policies
                },
            },
            'auth_keys': {
                k.name: k.to_api() for k in self.auth_policies
            },
        }
