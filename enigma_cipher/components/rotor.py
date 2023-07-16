"""
This module contains the Rotor class
"""
import string


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

    MAX_POSITIONS = len(string.ascii_uppercase)

    def __init__(self, position: int = 0):
        """
        Initializes the Rotor

        Parameters
        ----------
        position: int, default = 0
            Value of the position to the rotor that defines the character mapping.
            The maximum valid position is 35. Any position higher will take its wrapped
            analogous value. For example, position 50 is equivalent to position 14.
        """
        self.__current_pos = position % self.MAX_POSITIONS

    def update_position(self):
        """
        Updates the rotor position in 1, returning to position 0 when position 36
        is reached.
        """
        self.__current_pos = (self.__current_pos + 1) % self.MAX_POSITIONS

    @property
    def will_reset_position(self) -> bool:
        """bool: Whether the rotor will reset to position 0 in the next update"""
        return self.__current_pos == self.MAX_POSITIONS - 1

    def encode_character(self, character: str) -> str:
        """
        Encodes a single character in function of the current rotor position.

        Parameters
        ----------
        character: str
            Character to be encoded into a different one.

        Returns
        -------
        str:
            Encoded character as a new letter or digit.
        """
        character_idx = string.ascii_uppercase.index(character)
        encoded_char_idx = (character_idx + self.__current_pos) % self.MAX_POSITIONS
        return string.ascii_uppercase[encoded_char_idx]
