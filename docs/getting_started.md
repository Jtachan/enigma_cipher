# Getting started

First thing, import the package to your module:

```python
from enigma_cipher import EnigmaMachine
```

With that, now you can create your own `EnigmaMachine` instance, specifying the plugboard, the rotors and the reflector.
However, let's keep it simple.
To quickly use it, let's do a random initialization:

```python
cipher = EnigmaMachine.random_configuration()
```

Now the instance is ready to use.
The only thing left is to feed it the text or texts to cipher.

```python
cipher.cipher_text("Hello world!")
# 'OQOAX LBGBU!'
```

The term 'cipher' means to put a message through a code. 
Thus, the same machine can decode the message with the same command.

```python
cipher.cipher_text("OQOAX LBGBU!")
# 'HELLO WORLD!'
```

However, only machines with **the same configuration** can decode texts. 
Otherwise, you would be encoding another encoded text.

You might have encountered the case in which you followed this quick tutorial, and your results were totally different from the ones exposed here.
That is totally normal, as your EnigmaMachine would have a different configuration.

`EnigmaCipher` also allows you to initialize your machine from a given configuration saved in a .json file, or export your configuration so later on other machine can decode the texts that were previously encoded.

```python
# Export a configuration to a .json file
cipher.export_configuration_to_json_file("enigma_config.json")

# Initialize a machine from a configuration file
cipher = EnigmaMachine.from_configuration_file("enigma_config.json")
```

If you want to check everything is correct, you can download this [configuration file](../unittests/enigma_config.json) and initialize your machine with it. Then, try to decode the following text:

```commandline
ELGDZBZO! RRT BTA YQRV PJR NM DESXQF NVJZX CINME OAI ILWEPH ODEXUWB.
```
