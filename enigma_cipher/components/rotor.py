"""
This module contains the Rotor class
"""
import random
import string
from typing import Final


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

    MAX_POSITIONS: Final[int] = len(string.ascii_uppercase)

    def __init__(self, position: int = 0):
        """
        Initializes the Rotor

        Parameters
        ----------
        position: int, default = 0
            Value of the position to the rotor that defines the character mapping.
            The maximum valid position is 26. Any position higher will take its wrapped
            analogous value. For example, position 32 is equivalent to position 6.
        """
        self.__current_pos = position % self.MAX_POSITIONS

    @classmethod
    def random_init(cls):
        """Initializes the Rotor class in a random position"""
        return cls(random.randint(0, 26))

    def update_position(self):
        """
        Updates the rotor position in one unit, returning to position 0 when
        position 26 is reached.
        """
        self.__current_pos = (self.__current_pos + 1) % self.MAX_POSITIONS

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
        character_idx = string.ascii_uppercase.index(character)
        if is_forward_path:
            encoded_char_idx = (character_idx - self.__current_pos) % self.MAX_POSITIONS
        else:
            encoded_char_idx = (character_idx + self.__current_pos) % self.MAX_POSITIONS
        return string.ascii_uppercase[encoded_char_idx]

    @property
    def current_position(self) -> int:
        """int: The current position of the rotor"""
        return self.__current_pos
