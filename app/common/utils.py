"""
Common functions and classes.
"""

from typing import Dict


def unflatten_dict(dictionary: Dict):
    """
    Unflatten a dictionary with dot notation keys.
    """
    result: Dict = {}
    for key, value in dictionary.items():
        parts = key.split(".")
        dictionary = result
        for part in parts[:-1]:
            if part not in dictionary:
                dictionary[part] = {}
            dictionary = dictionary[part]
        dictionary[parts[-1]] = value
    return result
