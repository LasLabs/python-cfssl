# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from .config_mixer import ConfigMixer


class ConfigClient(ConfigMixer):
    """ It provides a Client Config compatible with CFSSL. """

    def __init__(self, sign_policy_default,
                 sign_policies_add, auth_policies, remotes):
        """ Initialize a new Client Configuration.

        Args:
            sign_policy_default (PolicySign): Default signing
                policy for client to use.
            sign_policies_add (tuple of PolicySign):
                Additional signing policies to use for the client.
            auth_policies (tuple of PolicyAuth): Auth
                policies for the client.
            remotes (tuple of Host): Remote hosts that
                client trusts.
        """
        super(ConfigClient, self).__init__(
            sign_policy_default, auth_policies, remotes,
        )
        self.remotes = remotes

    def to_api(self):
        """ It returns an object compatible with the API. """
        res = super(ConfigClient, self).to_api()
        res['remotes'] = {
            r.name: r.to_api() for r in self.remotes
        }
        return res
