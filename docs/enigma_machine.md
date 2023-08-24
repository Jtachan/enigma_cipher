# Enigma Machine

The `EnigmaMachine` allows to create a python instance to cipher texts.
It has to be composed by three parts: the [`PlugBoard`](plug_board.md), the [`Rotor`](rotor.md) and the [`Reflector`](reflector.md).
The settings of all three parts are defined as the machine's configuration.

The `EnigmaMachine` class can be imported directly from the `enigma_cipher` package:

```python
from enigma_cipher import EnigmaMachine
```

## `EnigmaMachine(plugboard, rotors, reflector, reset_after_ciphering=True)`

Constructor of the `EnigmaMachine` cipher.

_Parameters_

- **plugboard** `PlugBoard`:<br/>Component of the `PlugBoard`. It specifies the mapping among all the keys at the input/output level.
- **rotors** `Sequence of Rotor`:<br/>Initialized `Rotor` instances in a sequence. While the historic enigma machine contained only three rotors, the `EnigmaMachine` class can work with as many or few as desired.
- **reflector** `Reflector`:<br/>Component of the `Reflector`.
- **reset_after_ciphering** `bool` (default = True):<br/>Flag that controls if the machine should reset to the initial configuration after ciphering a text.

## `EnigmaMachine.cipher_text(text)`

Proceeds to cipher a given text.
Ciphering will decode an encoded text if the machine has the same configuration as the initial machine that encoded the text.

_Parameters_

- **text** `str`:<br/> Message to cipher (encode or decode) with the current configuration.

_Returns_

- `str`:<br/>The ciphered text.

## `EnigmaMachine.export_configuration_to_json_file(output_path, force=False)`

Export the machine configuration to a '.json' file.

_Parameters_

- **output_path** `str`:<br/>Path to the file to contain the configuration. Values as "path/to/file" will create a file "path/to/file.json".
- **force** `bool` (default = False):<br/>If True, allows overwriting existing output files. Otherwise, raises an error if the file already exists.

## Class methods

### `EnigmaMachine.random_configuration(nof_rotors=None, reset_after_ciphering=True)`

Initializes the machine and all its components with a random configuration.

_Parameters_

- **nof_rotors** `int` (optional):<br/>Number of rotors that compose the machine. If not specified, a randon number of them between 2 and 10 will be configured.
- **reset_after_ciphering** `bool` (default = True):<br/>Flag that controls if the machine should reset to the initial configuration after ciphering a text.

_Returns_

- `EnigmaMachine`:<br/>The instance initialized to a totally random configuration for all the elements.

### `EnigmaMachine.from_configuration(configuration, reset_after_ciphering=True)`

Initializes the machine from a specified configuration.

_Parameters_

- **configuration** `dict`:<br/>Mapping containing the machine configuration. It must be defined as the one returned in [`EnigmaMachine.initial_config`](#enigmamachineinitialconfiguration).
- **reset_after_ciphering** `bool` (default = True):<br/>Flag that controls if the machine should reset to the initial configuration after ciphering a text.

_Returns_

- `EnigmaMachine`:<br/>The instance initialized to the specified configuration.

### `EnigmaMachine.from_configuration_file(input_path, reset_after_ciphering=True)`

Initializes the machine from a .json configuration file.

_Parameters_

- **input_path** `str`:<br/>Path to the .json file containing the configuration.
- **reset_after_ciphering** `bool` (default = True):<br/>Flag that controls if the machine should reset to the initial configuration after ciphering a text.

_Returns_

- `EnigmaMachine`:<br/>The instance initialized to the specified configuration within the file.

## Properties

### `EnigmaMachine.initial_configuration`

_Returns_

- `dict`:<br/>Initial configuration as a dictionary with the keys 'plugboard', 'rotors' and 'reflector'.
