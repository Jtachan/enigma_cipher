"""
This module contains the PlugBoard dataclass
"""
from __future__ import annotations

import random
from typing import Mapping, Optional

from enigma_cipher.components.characters import Characters


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

    def __init__(
        self,
        plugged_keys: Optional[Mapping[str, str]] = None,
        include_digits: bool = False,
    ):
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
        include_digits: bool, default = False
            If True, the PlugBoard will include the digits to be ciphered. As default,
            only letters are to be ciphered.

        Raises
        ------
        PlugBoardError:
            If a letter is being mapped to different values or to a non-character and
            non-ascii value.
        """
        self.__characters_type = (
            Characters.ALPHANUMERIC if include_digits else Characters.ALPHABETIC
        )
        valid_characters_set = set(self.__characters_type.value)

        if plugged_keys is None:
            self._keys_map = {key: key for key in valid_characters_set}
        else:
            final_mapping = {key: "" for key in valid_characters_set}
            unused_keys = valid_characters_set.copy()

            for key, value in plugged_keys.items():
                key, value = key.upper(), value.upper()
                if key not in valid_characters_set or value not in valid_characters_set:
                    raise PlugBoardError(
                        "Invalid mapping given. Only the following characters "
                        f"are allowed:\n'{valid_characters_set}'"
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

            self._keys_map = final_mapping

    @classmethod
    def random_map(cls, include_digits: bool = False) -> PlugBoard:
        """
        Initializes the PlugBoard class with a random mapping. The mapping might
        contain all characters connected or only a few.

        Parameters
        ----------
        include_digits: bool, default = False
            If True, the PlugBoard will include the digits to be ciphered. As default,
            only letters are to be ciphered.
        """
        valid_characters = (
            list(Characters.ALPHANUMERIC.value)
            if include_digits
            else list(Characters.ALPHABETIC.value)
        )
        nof_characters = len(valid_characters)

        keys_map = {}
        shuffled_keys = iter(random.sample(valid_characters, nof_characters))
        for key, _ in zip(
            shuffled_keys, range(random.randint(0, int(nof_characters / 2)))
        ):
            keys_map[key] = next(shuffled_keys)

        return cls(plugged_keys=keys_map, include_digits=include_digits)

    def cipher_character(self, character: str) -> str:
        """
        Returns the mapped character on the plugboard
        """
        return self._keys_map[character]

    @property
    def plugged_keys(self) -> Mapping[str, str]:
        """Mapping: Configured keys mapping for all valid characters"""
        return dict(sorted(self._keys_map.items()))

    @property
    def contains_digits(self) -> bool:
        """bool: Whether if the component contains digits within its valid characters"""
        return self.__characters_type is Characters.ALPHANUMERIC
