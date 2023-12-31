"""
Module containing tests for the EnigmaMachine class
"""
import os
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
            cipher_config["plugboard"][key]
            == cipher.initial_configuration["plugboard"][key]
        ), f"Key '{key}' is not plugged to the correct one"

    for rotor_idx, (expected_rotor, configured_rotor) in enumerate(
        zip(cipher_config["rotors"], cipher.initial_configuration["rotors"])
    ):
        expected_rotor = expected_rotor % 26
        assert expected_rotor == configured_rotor, (
            f"Rotor {rotor_idx} should be in position {expected_rotor}, "
            f"but it is in position {configured_rotor} instead"
        )

    assert (
        cipher_config["reflector"] == cipher.initial_configuration["reflector"]
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


def test_digits_ciphering():
    """
    Testing the correct number ciphering. This implies two statements:
        1. A ciphered number will be a different alphanumeric character.
        2. The decoded text must still be retrieved.
    """
    cipher = EnigmaMachine.random_configuration(include_digits=True)
    text = "1 kg is 1000 g and 1 lb is 16 oz."
    encoded_text = cipher.cipher_text(text)

    assert encoded_text[0] != "1", "Digits not correctly encoded"
    assert text.upper() == cipher.cipher_text(encoded_text)


def test_init_from_file():
    """
    Checking correct initialization from a configuration file. If initialized
    correctly, the ciphered text (decoded) should read 'HELLO WORLD!'
    """
    cipher = EnigmaMachine.from_configuration_file(
        os.path.join("docs", "files", "enigma_config.json")
    )
    assert "HELLO WORLD!" == cipher.cipher_text("OQOAX LBGBU!")
