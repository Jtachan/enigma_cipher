"""
This module contains the PlugBoard dataclass
"""
from __future__ import annotations

import random
import string
from typing import Final, Mapping, Optional, Set


class PlugBoardError(ValueError):
    """
    Error to be raised if there is any conflict within the PlugBoard class
    """


class PlugBoard:
    """
    The PlugBoard provides the mapping of each letter to another one. Each letter
    can be mapped to another letter only once. Also, mapping the letter 'A' with the
    letter 'T' will block this combination, not allowing mapping the letter 'T' with
    any other letter.
    """

    VALID_CHARACTERS: Final[Set[str]] = set(string.ascii_uppercase)

    def __init__(self, plugged_keys: Optional[Mapping[str, str]] = None):
        """
        Initializes the class from a given mapping.

        Parameters
        ----------
        plugged_keys: Mapping, optional
            Mapping for every single letter. If not given, no mapping is defined,
            meaning letter 'A' is mapped to 'A' and so on.
            It is not necessary to specify both directions as {"A": "B", "B": "A"};
            the specification of {"A": "B", ...} is enough for the class to understand
            the connection is bidirectional.
            It is not needed to give all characters, only those that are mapped.

        Raises
        ------
        PlugBoardError:
            If a letter is being mapped to different values or to a non-character and
            non-ascii value.
        """
        if plugged_keys is None:
            self.__keys_map = {key: key for key in self.VALID_CHARACTERS}
        else:
            final_mapping = {key: "" for key in self.VALID_CHARACTERS}
            unused_keys = list(self.VALID_CHARACTERS)

            for key, value in plugged_keys.items():
                key, value = key.upper(), value.upper()
                if (
                    key not in self.VALID_CHARACTERS
                    or value not in self.VALID_CHARACTERS
                ):
                    raise PlugBoardError(
                        f"Invalid mapping given. Only characters "
                        f"'{self.VALID_CHARACTERS}' are allowed"
                    )
                if final_mapping[key] == value:
                    continue
                if final_mapping[key] != "":
                    raise PlugBoardError(
                        f"Key '{key}' mapped to '{value}' and '{final_mapping[key]}'."
                    )

                final_mapping[key], final_mapping[value] = value, key
                unused_keys.remove(key)
                if key != value:
                    unused_keys.remove(value)

            for key in unused_keys:
                final_mapping[key] = key

            self.__keys_map = final_mapping

    @classmethod
    def random_map(cls) -> PlugBoard:
        """
        Initializes the PlugBoard class with a random mapping. The mapping might
        contain all letters connected or only a few.
        """
        keys_map = {}
        shuffled_keys = iter(random.sample(list(cls.VALID_CHARACTERS), 26))
        for key, _ in zip(shuffled_keys, range(random.randint(0, 13))):
            keys_map[key] = next(shuffled_keys)

        return cls(plugged_keys=keys_map)

    def cipher_character(self, character: str) -> str:
        """
        Returns the mapped character on the plugboard
        """
        return self.__keys_map[character]

    @property
    def plugged_keys(self) -> Mapping[str, str]:
        """Mapping: Configured keys mapping for all valid characters"""
        return self.__keys_map
