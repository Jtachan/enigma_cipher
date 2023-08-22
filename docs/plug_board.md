# `enigma_cipher.PlugBoard`

The `PlugBoard` provides the mapping of each letter to another one. ach letter can be mapped to another letter only once.
Mapping the letter 'A' with the letter 'T' will block this combination, not allowing mapping the letter 'T' with any other letter.

## `PlugBoard(plugged_keys=None)`

Initializes the `PlugBoard` from the given mapping of keys.
It only takes alphabetic characters.

_Parameters_

- **plugged_keys** `Mapping[str, str]`, optional:<br/> Mapping for every single letter in pairs. It is not necessary to specify both directions as {"A": "B", "B": "A"}; the specification of {"A": "B", ...} is enough for the class to understand the connection is bidirectional. Any not specified letter is assumed as one without any connection to another letter. If not specified, all letters are plugged to themselves.

## `PlugBoard.cipher_character(character)`

_Parameters_

- **character** `str`:<br/>Letter to cipher through the component.

_Returns_

- `str`:<br/>The character ciphered only through the `PlugBoard`.

## Class methods

### `PlugBoard.random_map()`

_Returns_

- `PlugBoard`:<br/>Initializes the PlugBoard class with a random mapping among the letters.
The mapping can hold from no mapping among letters to having all letters mapped.

## Properties

### `PlugBoard.plugged_keys`

_Returns_

- `Mapping[str, str]`:<br/>Configured keys mapping for all valid characters.
