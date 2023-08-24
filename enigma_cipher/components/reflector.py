"""
This module contains the reflector class
"""
import random
import string
from typing import Dict, Final, Literal, Optional


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
        """
        if mode == "random":
            reflections = {}
            characters = iter(random.sample(string.ascii_uppercase, 26))
            for key in characters:
                if key in reflections:
                    continue

                value = next(characters)
                reflections[key] = value
                reflections[value] = key

            self.__reflections = reflections

        elif mode == "custom":
            if custom_map is None:
                raise ReflectorError(
                    "Mode 'custom' was given, but no map was specified."
                )
            self.__reflections = custom_map

        else:
            self.__reflections = Reflector._HISTORICAL_VALUES

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
        return self.__reflections[character]

    @property
    def reflections_map(self) -> dict:
        """dict: Map that composes the reflector"""
        return self.__reflections

    @property
    def is_historical(self) -> bool:
        """
        bool: Whether the current reflector is defined in the historical configuration
        """
        return self.__reflections == Reflector._HISTORICAL_VALUES
