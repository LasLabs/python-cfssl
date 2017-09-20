# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


def to_api(_object):
    """Ensure an object is converted using its ``to_api`` method if it exists.

    Args:
        _object (object): Object to convert to API, or simply return.
    Returns:
       dict: A dictionary representation of the object that is compatible with
        the CFSSL server API.
    """
    try:
        return _object.to_api()
    except AttributeError:
        return _object
