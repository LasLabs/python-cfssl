# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


def to_api(object):
    """ Ensure an object is converted using it's to_api method if it exists.

    Args:
        object (any):
    Returns:
        str: A PEM-encoded certificate that has been signed by the
            server.
    """
    return object.to_api() if hasattr(object, 'to_api') else object