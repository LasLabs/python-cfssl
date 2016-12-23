# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class SubjectInfo(object):
    """ It provides a SubjectInfo (Name) compatible with CFSSL. """

    def __init__(self, org_name, org_unit, city, state, country):
        """ Initialize a new Subject Information.

        Args:
            org_name (str): The full legal name of the organization. Do
                not abbreviate.
            org_unit (str): Section of the organization.
            city (str): The city where the organization is legally
                located.
            country (str): The two letter ISO abbreviation for the
                country.
        """
        self.org_name = org_name
        self.org_unit = org_unit
        self.city = city
        self.state = state
        self.country = country

    def to_api(self):
        """ It returns an object compatible with the API. """
        return {
            'O': self.org_name,
            'OU': self.org_unit,
            'L': self.city,
            'ST': self.state,
            'C': self.country,
        }
