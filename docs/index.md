# Enigma Cipher

`EnigmaCipher` is a package that allows you to cipher (encode and/or decode) texts by using the Enigma Machine's logic.

## Why to use EnigmaCipher to cipher texts

- **Easy to use**: The instance only needs to know the text to cipher and will return a text.
- **No reinitialization**: After ciphering a text, the instance can be used again to decode texts encoded with the same configuration.
- **Infinite configurations**: The cipher can be set on multiple configurations which deviate from the historical machine. For example, with six rotors (instead of three) or with every single component randomly initialized.

## Setup

_Requirements_

- Python 3.8 or higher

_Installation_

The package's latest release can be installed via pip:

```commandline
pip install enigma-cipher
```

If you wish to work with the latest unreleased changes, install the 'develop' branch:

```commandline
pip install git+https://github.com/Jtachan/enigma_cipher.git@develop
```

## Index

- First steps
- Components
- Enigma Machine
