"""
This module contains the reflector class
"""
import random
from typing import Dict, Final, Literal, Optional

from enigma_cipher.components.characters import Characters


class ReflectorError(ValueError):
    """Error to be raised if the reflector fails"""


class Reflector:
    """
    The reflector connects, in pairs, all the positions of the letters. This allows
    that an encoded text could be decoded with a machine having the same PlugBoard
    and Rotors configuration.
    """

    _HISTORICAL_VALUES: Final[Dict[str, str]] = {
        "A": "E",
        "B": "J",
        "C": "M",
        "D": "Z",
        "E": "A",
        "F": "L",
        "G": "Y",
        "H": "X",
        "I": "V",
        "J": "B",
        "K": "W",
        "L": "F",
        "M": "C",
        "N": "R",
        "O": "Q",
        "P": "U",
        "Q": "O",
        "R": "N",
        "S": "T",
        "T": "S",
        "U": "P",
        "V": "I",
        "W": "K",
        "X": "H",
        "Y": "G",
        "Z": "D",
    }

    def __init__(
        self,
        mode: Literal["random", "historical", "custom"] = "historical",
        custom_map: Optional[Dict[str, str]] = None,
        include_digits: bool = False,
    ):
        """
        Initializes the reflector

        Parameters
        ----------
        mode: Literal str
            String defining the key mapping of the reflector.
                - 'random': The map among the letters is totally random.
                - 'historical' (default): The historical reflector is used.
                - 'custom': Allows setting a specific reflector configuration.
        custom_map: dict, optional
            Mapping of all characters.
            The characters must be specified in uppercase, and each letter must be
            paired to only one another letter.
        include_digits: bool, default = False
            If True, the Reflector will include the digits to be ciphered. As default,
            only letters are to be ciphered.
            This value is only considered for 'random' mode, as its value is computed
            for 'custom' mode and set to False for 'historical' mode.
        """
        if mode not in {"random", "historical", "custom"}:
            raise ReflectorError(f"Invalid mode '{mode}' given.")

        if mode == "random":
            self.__valid_characters = (
                Characters.ALPHANUMERIC if include_digits else Characters.ALPHABETIC
            )

            reflections = {}
            characters = iter(
                random.sample(
                    list(self.__valid_characters.value),
                    len(self.__valid_characters.value),
                )
            )
            for key in characters:
                if key in reflections:
                    continue

                value = next(characters)
                reflections[key] = value
                reflections[value] = key

            self._reflections = reflections

        elif mode == "custom":
            if custom_map is None:
                raise ReflectorError(
                    "Mode 'custom' was given, but no map was specified."
                )
            alphanumeric_characters = Characters.ALPHANUMERIC.value
            for key in custom_map:
                if key not in alphanumeric_characters:
                    raise ReflectorError(f"Invalid character '{key}' given")

            if set(custom_map.keys()) == alphanumeric_characters:
                self.__valid_characters = Characters.ALPHANUMERIC
            else:
                self.__valid_characters = Characters.ALPHABETIC

            self._reflections = custom_map

        else:
            self.__valid_characters = Characters.ALPHABETIC
            self._reflections = Reflector._HISTORICAL_VALUES

    def reflect_character(self, character: str) -> str:
        """
        Returns the reflection of a given character.

        Parameters
        ----------
        character: str
            Initial letter to be reflected

        Returns
        -------
        str:
            Reflection of the given letter.
        """
        return self._reflections[character]

    @property
    def reflections_map(self) -> dict:
        """dict: Map that composes the reflector"""
        return dict(sorted(self._reflections.items()))

    @property
    def is_historical(self) -> bool:
        """
        bool: Whether the current reflector is defined in the historical configuration
        """
        return self._reflections == Reflector._HISTORICAL_VALUES

    @property
    def contains_digits(self) -> bool:
        """bool: Whether if the Reflector contains digits as valid characters"""
        return self.__valid_characters is Characters.ALPHANUMERIC
