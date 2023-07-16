"""
This module contains the StackerBoard dataclass
"""
import string
from typing import Mapping, Optional


class StackerBoardError(ValueError):
    """
    Error to be raised if there is any conflict within the StackerBoard class
    """


class StackerBoard:
    """
    The StackerBoard provides the mapping of each letter to another one. Each letter
    can be mapped to another letter only once. Also, mapping the letter 'A' with the
    letter 'T' will block this combination, not allowing mapping the letter 'T' with
    any other letter.

    In difference to the original 'stackerbett' from the Enigma Machine, this one
    allows mapping also numbers.
    """

    VALID_CHARACTERS = list(string.ascii_lowercase)

    def __init__(self, keys_map: Optional[Mapping[str, str]] = None):
        """
        Initializes the class from a given mapping.

        Parameters
        ----------
        keys_map: Mapping, optional
            Mapping for every single letter. It is not necessary to specify both
            directions as {"A": "B", "B": "A"}; the specification of {"A": "B", ...} is
            enough for the class to understand the connection is bidirectional.
            If not given, no mapping is defined, meaning letter 'A' is mapped to 'A'
            and so on.

        Raises
        ------
        StackerBoardError:
            If a letter is being mapped to different values or to a non-character and
            non-ascii value.
        """
        if keys_map is not None and len(keys_map) > 0:
            final_mapping = {key: "" for key in self.VALID_CHARACTERS}
            for key in self.VALID_CHARACTERS:
                if value := keys_map.get(key, keys_map.get(key.upper())) is None:
                    continue
                value = str(value)
                if len(value) not in self.VALID_CHARACTERS:
                    raise StackerBoardError(
                        f"Invalid map '{key} -> {value}' specified."
                    )
                if final_mapping[value] not in ("", key):
                    raise StackerBoardError(
                        f"Key '{value}' mapped to '{key}' and '{final_mapping[value]}'."
                    )

                final_mapping[key] = value
                final_mapping[value] = key

            self.__keys_map = final_mapping

        else:
            self.__keys_map = {key: key for key in self.VALID_CHARACTERS}

    @property
    def keys_map(self) -> Mapping[str, str]:
        """Mapping: Configured keys mapping for all valid characters"""
        return self.__keys_map
