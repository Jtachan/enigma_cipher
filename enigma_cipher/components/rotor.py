"""
This module contains the Rotor class
"""
from __future__ import annotations

import random

from enigma_cipher.components.characters import Characters


class Rotor:
    """
    This class represents one of the rotors contained within the Enigma Machine.
    Each rotor contains a position that defines a letter mapping. After a letter is
    pressed, the rotor steps up one position. After the rotor has spun all character
    positions (the whole alphabet), the next rotor will step up one position.

    Mapping examples
    ----------------
    Position 0: 'A' = 'A'
    Position 1: 'A' = 'B'
    ...
    Position 5: 'A' = 'E'
    """

    def __init__(self, position: int = 0, include_digits: bool = False):
        """
        Initializes the Rotor

        Parameters
        ----------
        position: int, default = 0
            Value of the position to the rotor that defines the character mapping.
            The maximum valid position is 26. Any position higher will take its wrapped
            analogous value. For example, position 32 is equivalent to position 6,
            counting only with alphabetic characters.
        include_digits: bool, default = False
            If True, the Rotor will include the digits to be ciphered. This also
            affects the number of os positions the rotor can have. As default, only
            letters are to be ciphered.
        """
        characters_type = (
            Characters.ALPHANUMERIC if include_digits else Characters.ALPHABETIC
        )
        self.__valid_characters = characters_type.value.copy()
        self.__max_positions = len(self.__valid_characters)

        self._current_pos = position % self.__max_positions

    @classmethod
    def random_init(cls, include_digits: bool = False) -> Rotor:
        """
        Initializes the Rotor class in a random position

        Parameters
        ----------
        include_digits: bool, default = False
            If True, the Rotor will include the digits to be ciphered. This also
            affects the number of os positions the rotor can have. As default, only
            letters are to be ciphered.
        """
        nof_characters = len(
            Characters.ALPHANUMERIC.value
            if include_digits
            else Characters.ALPHABETIC.value
        )
        return cls(
            position=random.randint(0, nof_characters), include_digits=include_digits
        )

    def update_position(self):
        """
        Updates the rotor position in one unit, returning to position 0 when
        position 26 is reached.
        """
        self._current_pos = (self._current_pos + 1) % self.__max_positions

    def cipher_character(self, character: str, is_forward_path: bool) -> str:
        """
        Ciphers a single character in function of the current rotor position.

        Parameters
        ----------
        character: str
            Character to be ciphered.
        is_forward_path: bool
            Evaluates if the path of ciphering is forward (from input to reflector)
            or backwards (from reflector to output).

        Returns
        -------
        str:
            Ciphered character as a new letter.
        """
        character_idx = self.__valid_characters.index(character)
        if is_forward_path:
            encoded_char_idx = (
                character_idx - self._current_pos
            ) % self.__max_positions
        else:
            encoded_char_idx = (
                character_idx + self._current_pos
            ) % self.__max_positions
        return self.__valid_characters[encoded_char_idx]

    @property
    def current_position(self) -> int:
        """int: The current position of the rotor"""
        return self._current_pos

    @property
    def contains_digits(self) -> bool:
        """bool: Whether if the Rotor contains digits as valid characters to cipher"""
        return self.__max_positions == 36
