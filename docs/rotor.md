# Rotor

The `Rotor` provide a _shift-ciphering_ based on the rotor's position.
A rotor at position 0 will map a character with itself, for example, "E" = "E".
A rotor at position 3 will map a character with the one three positions ahead, for example, "E" = "H".

After ciphering a character, the first rotor will update its position in 1.
The next rotors will update their position when the previous rotor has done a full spin.

The `Rotor` class can be imported directly from the `enigma_cipher` package:

```python
from enigma_cipher import Rotor
```

## `Rotor(position=0)`

Initializes the `Rotor` instance at the specified position.

_Parameters_

- **position** `int`:<br/>Position in the range [0, 25] in which the rotor is initialized. Any given position higher than 25 is set to its equivalent within the range, for example, `position=32` is the same as `position=6`. If the position is not specified, the rotor is initialized at `position=0`.

## `Rotor.update_position()`

Updates the rotor position in one unit, returning to position 0 when position 26 is reached.

## `Rotor.cipher_character(character, is_forward_path)`

Ciphers a single character through the current `Rotor` instance.

_Parameters_

- **character** `str`:<br/>Character to be ciphered.
- **is_forward_path** `bool`:<br/>Evaluates if the path of ciphering is forward (from input to reflector) or backwards (from reflector to output).

_Returns_

- `str`:<br/>Ciphered character as the same or a new letter.

## Class methods

### `Rotor.random_init()`

_Returns_

- `Rotor`:<br/>Instance initialized in a position within the range [0, 25].

## Properties

### `Rotor.current_position`

_Returns_

- `int`:<br/>The current position of the rotor.
