# `enigma_cipher.PlugBoard`

The `PlugBoard` provides the mapping of each letter to another one. ach letter can be mapped to another letter only once.
Mapping the letter 'A' with the letter 'T' will block this combination, not allowing mapping the letter 'T' with any other letter.

The `PlugBoard` class can be imported directly from the `enigma_cipher` package:

```python
from enigma_cipher import PlugBoard
```

## `PlugBoard(plugged_keys=None, include_digits=False)`

Initializes the `PlugBoard` from the given mapping of keys.
It only takes alphabetic characters.

_Parameters_

- **plugged_keys** `Mapping[str, str]`, optional:<br/> Mapping for every single letter in pairs. It is not necessary to specify both directions as {"A": "B", "B": "A"}; the specification of {"A": "B", ...} is enough for the class to understand the connection is bidirectional. Any not specified letter is assumed as one without any connection to another letter. If not specified, all letters are plugged to themselves.
- **include_digits** `bool`, default = False:<br/>If True, the PlugBoard will include the digits to be ciphered. As default, only letters are to be ciphered.

## `PlugBoard.cipher_character(character)`

_Parameters_

- **character** `str`:<br/>Letter to cipher through the component.

_Returns_

- `str`:<br/>The character ciphered only through the `PlugBoard`.

## Class methods

### `PlugBoard.random_map(include_digits=False)`

Initializes the PlugBoard class with a random mapping. 
The mapping might contain all characters connected or only a few.

_Parameters_

**include_digits**: `bool`, default = False:<br/> If True, the PlugBoard will include the digits to be ciphered. As default, only letters are to be ciphered.

_Returns_

- `PlugBoard`:<br/>Initializes the PlugBoard class with a random mapping among the characters.

## Properties

### `PlugBoard.plugged_keys`

_Returns_

- `Mapping[str, str]`:<br/>Configured keys mapping for all valid characters.

### `PlugBoard.contains_digits`

_Returns_

- `bool`:<br/>Whether if the component contains digits within its valid characters
