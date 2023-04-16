"""
Main module of the application.
"""

from app.common.utils import unflatten_dict


def main():
    """
    Entry point for the application script
    """
    sample_dict = {
        "a.b.c": 1,
        "a.b.d": 2,
        "a.e": 3,
        "f": 4,
    }

    result = unflatten_dict(sample_dict)

    print(result)


main()
