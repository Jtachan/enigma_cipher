![tests_badge](https://github.com/Jtachan/enigma_cipher/actions/workflows/unittests.yml/badge.svg)
![docs_badge](https://github.com/Jtachan/enigma_cipher/actions/workflows/docs.yml/badge.svg)

# Enigma Cipher

The `Enigma Cipher` is a package that allows ciphering texts as an enigma machine would.

It is referred to 'cipher' the text instead of encoding/decoding, as any text can be encoded or decoded bz ciphering it with a machine with the same configuration.
For example, if the text `VLGBR OYWVV!` is ciphered through a machine with the correct configuration, the outcome will be `HELLO WORLD!`

## 📖 Documentation

You can find the documentation:

- Within the [`/docs`](docs/index.md) folder
- At the [mkdocs generated page](https://jtachan.github.io/enigma_cipher/) (official documentation)

## 🐍 Python Setup

**Requirements**

- Python 3.8 or higher

**Installation**

Use pip with the git link to the repo:
````commandline
pip install git+https://github.com/Jtachan/enigma_cipher.git
````

The 'develop' branch can also be installed to work with unreleased features:
````commandline
pip install git+https://github.com/Jtachan/enigma_cipher.git@develop
````

