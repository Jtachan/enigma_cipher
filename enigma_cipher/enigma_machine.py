"""
This module contains the EnigmaMachine class
"""
from __future__ import annotations

import json
import os
import random
from typing import Optional, Sequence

from enigma_cipher.components.plug_board import PlugBoard
from enigma_cipher.components.reflector import Reflector
from enigma_cipher.components.rotor import Rotor


class EnigmaMachine:
    """
    This class allows encoding and decoding text messages. Only alphabetic characters
    are encoded, other characters are returned as they are.
    """

    def __init__(
        self,
        plugboard: PlugBoard,
        rotors: Sequence[Rotor],
        reflector: Reflector,
        reset_after_ciphering: bool = True,
    ):
        """
        Initializes the cipher

        Parameters
        ----------
        plugboard: PlugBoard
            Component of the plugboard. It specifies the mapping among all the keys
            at the input/output level.
        rotors: sequence of Rotors
            Initialized Rotor instances. While the historic enigma machine contained
            only three rotors, this parameter allows setting as many or few as desired.
        reflector: Reflector
            Component of the reflector.
        reset_after_ciphering: bool, default = True.
            If True, the machine instance will reset to the initialized configuration
            after ciphering a test.
        """
        if reflector.is_historical:
            reflector_config = "historical"
        else:
            reflector_config = reflector.reflections_map

        self.__init_config = {
            "plugboard": plugboard.plugged_keys,
            "rotors": [rotor.current_position for rotor in rotors],
            "reflector": reflector_config,
        }

        self.__plugboard = plugboard
        self.__rotors = rotors
        self.__reflector = reflector
        self.__reset = reset_after_ciphering

    @classmethod
    def from_configuration(
        cls, configuration: dict, reset_after_ciphering: bool = True
    ) -> EnigmaMachine:
        """
        Initializes the Cipher from a specific configuration.

        Parameters
        ----------
        configuration: dict
            Configuration defined in a dictionary, which must be similar to the one
            returned by EnigmaMachine.initial_config
        reset_after_ciphering: bool, default = True.
            If True, the machine instance will reset to the initialized configuration
            after ciphering a test.
        """
        if isinstance(reflector_config := configuration["reflector"], dict):
            reflector = Reflector(mode="custom", custom_map=reflector_config)
        elif reflector_config in ("random", "historical"):
            reflector = Reflector(mode=reflector_config)
        else:
            raise ValueError("Unknown configuration for reflector")

        return cls(
            plugboard=PlugBoard(configuration["plugboard"]),
            rotors=[Rotor(pos) for pos in configuration["rotors"]],
            reflector=reflector,
            reset_after_ciphering=reset_after_ciphering,
        )

    @classmethod
    def from_configuration_file(
        cls, input_path: str, reset_after_ciphering: bool = True
    ) -> EnigmaMachine:
        """
        Initializes the Cipher from a '.json' configuration file.

        Parameters
        ----------
        input_path: str
            Path to the file containing the configuration.
        reset_after_ciphering: bool, default = True.
            If True, the machine instance will reset to the initialized configuration
            after ciphering a test.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Not found file '{input_path}'.")
        if os.path.splitext(input_path)[-1].lower() != ".json":
            raise ValueError("The specified file is not the correct extension.")

        with open(input_path, "r", encoding="utf-8") as input_file:
            config_dict = json.load(input_file)

        return cls.from_configuration(
            configuration=config_dict, reset_after_ciphering=reset_after_ciphering
        )

    @classmethod
    def random_configuration(
        cls,
        nof_rotors: Optional[int] = None,
        reset_after_ciphering: bool = True,
    ) -> EnigmaMachine:
        """
        Initializes the EnigmaMachine from a totally random configuration.

        Parameters
        ----------
        nof_rotors: int, optional
            Number of rotors to be contained within the machine. If not specified,
            a randon number of them between 2 and 10 will be configured.
        reset_after_ciphering: bool, default = True.
            If True, the machine instance will reset to the initialized configuration
            after ciphering a test.
        """
        if nof_rotors is None:
            nof_rotors = random.randint(2, 10)

        return cls(
            plugboard=PlugBoard.random_map(),
            rotors=[Rotor(random.randint(0, 26)) for _ in range(nof_rotors)],
            reflector=Reflector(mode="random"),
            reset_after_ciphering=reset_after_ciphering,
        )

    def export_configuration_to_json_file(self, output_path: str, force: bool = False):
        """
        Exports the machine configuration to a '.json' file.

        Parameters
        ----------
        output_path: str
            Path to the file to contain the configuration.
            It is not necessary to specify the file extension.
        force: bool, default = False
            If True, allows overwriting existing output files.
        """
        output_path = os.path.splitext(output_path)[0] + ".json"

        if os.path.exists(output_path) and not force:
            raise FileExistsError("The specified file already exist.")

        with open(output_path, "w", encoding="utf-8") as out_file:
            json.dump(self.__init_config, out_file, indent=2)

        print(f"Configuration exported to '{output_path}'")

    def cipher_text(self, text: str) -> str:
        """
        Proceeds to cipher a given text.
        Ciphering will decode an encoded text if the machine has the same
        configuration as the initial machine that encoded the text.

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
                character = self._compute_forward(character)
                character = self._compute_backwards(character)
                self.__step_up_rotors()

            final_text += character

        # Reset the machine: only the rotors have changed from the original config.
        if self.__reset:
            self.__rotors = [Rotor(pos) for pos in self.__init_config["rotors"]]

        return final_text

    def _compute_forward(self, character: str) -> str:
        """
        Computes the cipher of a character from the input keyboard to the reflector.
        The class is called internally.

        Parameters
        ----------
        character: str
            Alphabetic character to cipher.

        Returns
        -------
        character: str
            Ciphered character.
        """
        character = self.__plugboard.cipher_character(character)
        for rotor in self.__rotors:
            character = rotor.cipher_character(character, is_forward_path=True)
        character = self.__reflector.reflect_character(character)

        return character

    def _compute_backwards(self, character: str) -> str:
        """
        Computes the cipher of a character from the reflector to the output.
        The class is called internally.

        Parameters
        ----------
        character: str
            Alphabetic character to cipher. This should be the output from the
            reflector.

        Returns
        -------
        character: str
            Ciphered character.
        """
        for rotor in self.__rotors[::-1]:
            character = rotor.cipher_character(character, is_forward_path=False)
        character = self.__plugboard.cipher_character(character)
        return character

    def __step_up_rotors(self):
        """
        The position of all rotors needed is updated by following the next rules:
            - The first rotor is always updated.
            - The following rotors are updated only if the previous has spun a
              complete turn.
            - Any update refers always to a single-step up in the rotor's position.
        """
        update_next_rotor = True
        for rotor in self.__rotors:
            update_rotor = update_next_rotor
            update_next_rotor = rotor.current_position == Rotor.MAX_POSITIONS - 1
            if update_rotor:
                rotor.update_position()

    @property
    def initial_configuration(self) -> dict:
        """
        dict: Initial configuration as a dictionary with the following keys:
            - 'plugboard': Contains the plugged keys.
            - 'rotors': Iteration of all rotor's initial positions.
            - 'reflector': Contains the reflector map.
        """
        return self.__init_config
