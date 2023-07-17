"""
This module contains the EnigmaCipher class
"""
from typing import Tuple

from enigma_cipher.components.plug_board import PlugBoard
from enigma_cipher.components.reflector import Reflector
from enigma_cipher.components.rotor import Rotor


class EnigmaCipher:
    """
    This class allows encoding and decoding text messages. Only alphabetic characters
    are encoded, other characters are returned as they are.
    """

    def __init__(
        self,
        plugboard: PlugBoard,
        rotors: Tuple[Rotor, Rotor, Rotor],
        reflector: Reflector,
    ):
        """
        Initializes the cipher

        Parameters
        ----------
        plugboard: PlugBoard
            Component of the original plugboard.
        rotors: tuple of three rotors
            Three initialized Rotor classes.
        reflector: Reflector
            Component of the reflector
        """

        self.__plugboard = plugboard
        self.__rotors = rotors
        self.__reflector = reflector

    def compute_forward(self, character: str) -> str:
        character = self.__plugboard.encode_character(character)

        for rotor in self.__rotors:
            character = rotor.encode_character(character, is_forward_path=True)

        character = self.__reflector.reflect_character(character)

        return character

    def compute_backwards(self, character: str) -> str:
        for rotor in self.__rotors[::-1]:
            character = rotor.encode_character(character, is_forward_path=False)

        character = self.__plugboard.encode_character(character)
        return character

    def __step_up_rotors(self):
        update_next_rotor = True
        for rotor in self.__rotors:
            update_rotor = update_next_rotor
            update_next_rotor = rotor.will_reset_position
            if update_rotor:
                rotor.update_position()

    def compute_text(self, text: str) -> str:
        """
        Computes a given text

        Parameters
        ----------
        text: str
            Message to cipher (encode or decode) with the current configuration.

        Returns
        -------
        str:
            Ciphered message. If the initial message was decoded, this would be encoded.
            Otherwise, this text is the decoded one.
        """
        final_text = ""
        for character in text.upper():
            if character.isalpha():
                character = self.compute_forward(character)
                character = self.compute_backwards(character)
                self.__step_up_rotors()

            final_text += character

        return final_text


if __name__ == "__main__":
    cipher = EnigmaCipher(
        plugboard=PlugBoard({"A": "F", "J": "K", "T": "M"}),
        rotors=(
            Rotor(position=0),
            Rotor(position=3),
            Rotor(position=7),
        ),
        reflector=Reflector("historical"),
    )

    print(cipher.compute_text("Q PYIC QWQ, NVBRB"))
