# coding=utf-8
"""

"""

from datetime import date, datetime
from math import ceil
import json


def clean_kwargs(ignored_keys, data):
    """
    Removes the ignored_keys from the data sent

    ignored_keys: keys to remove from the data (list or tuple)
    data: data to be cleaned (dict)

    returns: cleaned data
    """

    for key in ignored_keys:
        data.pop(key, None)

    return data


def roundUp(n, d=2):
    d = int('1' + ('0' * d))
    return ceil(n * d) / d


def populate_obj(obj, data):
    """
    Populates an object with the data passed to it

    param obj: Object to be populated
    param data: The data to populate it with (dict)

    returns: obj populated with data


    """
    for name, value in data.items():
        if hasattr(obj, name):
            # print(name, value)
            if isinstance(value, float):
                value = roundUp(value)
            setattr(obj, name, value)

    return obj
