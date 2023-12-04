# coding=utf-8
"""

"""


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
