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

## `Rotor(position=0, include_digits=False)`

Initializes the `Rotor` instance at the specified position.

_Parameters_

- **position** `int`:<br/>Position in the range [0, 25] in which the rotor is initialized. Any given position higher than 25 is set to its equivalent within the range, for example, `position=32` is the same as `position=6`. If the position is not specified, the rotor is initialized at `position=0`.
- **include_digits** `bool`, default = False:<br/>If True, the Rotor will include the digits to be ciphered. This also affects the number of os positions the rotor can have. The index of the first digit (zero) is 26, meaning digits are sorted after letters. As default, only letters are to be ciphered.

## `Rotor.update_position()`

Updates the rotor position in one unit, returning to position 0 when the last position is reached.

## `Rotor.cipher_character(character, is_forward_path)`

Ciphers a single character through the current `Rotor` instance.

_Parameters_

- **character** `str`:<br/>Character to be ciphered.
- **is_forward_path** `bool`:<br/>Evaluates if the path of ciphering is forward (from input to reflector) or backwards (from reflector to output).

_Returns_

- `str`:<br/>Ciphered character as the same or a new letter.

## Class methods

### `Rotor.random_init(include_digits=False)`

_Parameters_

- **include_digits** `bool`, default = False:<br/>If True, the Rotor will include the digits to be ciphered. This also affects the number of os positions the rotor can have. As default, only letters are to be ciphered.

_Returns_

- `Rotor`:<br/>Instance initialized in a position within the range [0, 25].

## Properties

### `Rotor.current_position`

_Returns_

- `int`:<br/>The current position of the rotor.

### `Rotor.contains_digits`

_Returns_

- `bool`:<br/>Whether if the component contains digits within its valid characters
