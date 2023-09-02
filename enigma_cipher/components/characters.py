"""
This module contains the Characters enum.
"""
import enum
import string


@enum.unique
class Characters(enum.Enum):
    """
    Enumeration containing the possible characters to encode within the cipher.
    """

    ALPHABETIC = {string.ascii_uppercase}
    ALPHANUMERIC = {string.ascii_uppercase + string.digits}
