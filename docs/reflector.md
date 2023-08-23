# Reflector

The reflector connects, in pairs, all the positions of the letters. This allows that an encoded text could be decoded with a machine having the same PlugBoard and Rotors configuration.

The `Reflector` class can be imported directly from the `enigma_cipher` package:

```python
from enigma_cipher import Reflector
```

## `Reflector(mode="historical", custom_map=None)`

Initializes the reflector instance.

_Parameters_

- **mode** `Literal str`:<br/>String defining the mapping of the reflector. The choices are:
<br/>`'historical'` (default): The historical reflector (the one used at the original machine) is set.
<br/>`'random'`: The map among the letters is totally random.
<br/>`'custom'`: Allows setting a specific reflector configuration.
- **custom_map** `dict`:<br/>Mapping of all characters. The mapping is only needed if `mode='custom'` is chosen. The characters must be specified in uppercase, and each letter must be paired to only one another letter.

## `Reflector.reflect_character(character)`

Returns the reflection of a given character.

_Parameters_

- **character** `str`:<br/>Character to be reflected.

_Returns_

- `str`:<br/>Reflection of the given letter.

## Properties

### `Reflector.reflections_map`

_Returns_

- `dict`:<br/>Map that composes the reflector

### `Reflector.is_historical`

_Returns_

- `bool`:<br/>Whether the current reflector is defined in the historical configuration.
