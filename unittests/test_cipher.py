"""
Module containing tests for the EnigmaMachine class
"""
import random

import pytest

from enigma_cipher import EnigmaMachine


def test_cipher_configuration():
    """
    This test checks that the Machine is defined with the given configuration.
    """
    cipher_config = {
        "plugboard": {"A": "T", "F": "J", "H": "L"},
        "rotors": [10, 0, 52],
        "reflector": "historical",
    }
    cipher = EnigmaMachine.from_configuration(cipher_config)

    for key in cipher_config["plugboard"]:
        assert (
            cipher_config["plugboard"][key] == cipher.configuration["plugboard"][key]
        ), f"Key '{key}' is not plugged to the correct one"

    for rotor_idx, (expected_rotor, configured_rotor) in enumerate(
        zip(cipher_config["rotors"], cipher.configuration["rotors"])
    ):
        expected_rotor = expected_rotor % 26
        assert expected_rotor == configured_rotor, (
            f"Rotor {rotor_idx} should be in position {expected_rotor}, "
            f"but it is in position {configured_rotor} instead"
        )

    assert (
        cipher_config["reflector"] == cipher.configuration["reflector"]
    ), "Reflector is not the correct one"


@pytest.mark.parametrize("nof_rotors", [random.randint(2, 10) for _ in range(5)])
def test_message_reflection(nof_rotors: int):
    """
    Checking a message can be encoded and decoded with a machine with the same
    configuration
    """
    cipher = EnigmaMachine.random_configuration(nof_rotors)
    text = "This is an enigma machine"

    encoded_text = cipher.cipher_text(text)
    assert text == cipher.cipher_text(encoded_text).capitalize()
