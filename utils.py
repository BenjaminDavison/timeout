"""
Generic utils
"""
import json


def _clean_input(json_input):
    """
    There are uppercase and lowercase mismatches in the users/venues.json file.
    This just makes everything lowercase.

    Just change the values in place.

    :param json_input:
    """
    for elem in json_input:
        for k,v in elem.items():
            if isinstance(v, list):
                elem[k] = [f.lower() for f in v]

    return json_input


def load_input(file_name):
    """
    Loads the selected user/venues.json file, and then returns a dict with everything
    lowercased.

    todo: error handling if .json file is corrupt

    :param file_name:
    """
    try:
        with open(file_name, 'r') as f:
            # clean json
            return _clean_input(json.load(f))
    except FileNotFoundError as exc:
        raise FileNotFoundError
