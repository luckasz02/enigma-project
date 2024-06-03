# Enigma Machine and Bombe Simulator

![Enigma Machine](https://en.wikipedia.org/wiki/Enigma_machine#/media/File:Enigma_(crittografia)_-_Museo_scienza_e_tecnologia_Milano.jpg)

## Overview

This project simulates the iconic Enigma Machine and the Bombe, a device used for deciphering encoded messages. The Enigma Machine was extensively used by Nazi Germany during World War II, while the Bombe was an electromechanical device used by the Allies to decrypt Enigma-encrypted messages.

## Features

- **Enigma Machine Simulation**: Encode and decode messages using configurable rotors and reflectors.
- **Bombe Simulation**: Perform a brute-force attack to determine the initial rotor settings for a given encoded message and known plaintext.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Running the Enigma Machine](#running-the-enigma-machine)
  - [Changing the Message](#changing-the-message)
  - [Bombe Attack](#bombe-attack)
- [Testing](#testing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/luckasz02/enigma-project.git
   cd Enigma
   ```

2. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Enigma Machine

To encode or decode a message using the Enigma Machine, run the `main.py` script:

```bash
python main.py
```

By default, it encodes and decodes the message "HELLO" using the initial rotor settings.

### Changing the Message

To change the message, edit the `main.py` file:

```python
message = "YOUR MESSAGE"
```

### Bombe Attack

To perform a Bombe attack and find the correct rotor settings for a given encoded message and known plaintext, use the `bombe_attack` function in the `bombe.py` module.

Example usage:

```python
from bombe import bombe_attack

if __name__ == "__main__":
    ciphertext = "EBYHM"
    known_plaintext = "HELLO"
    enigma = EnigmaMachine([...])  # Configure your Enigma machine here

    positions, decoded_message = bombe_attack(enigma, ciphertext, known_plaintext)
    if positions:
        print(f"Found positions: {positions} with decoded message: {decoded_message}")
    else:
        print("No valid settings found.")
```

## Testing

To run the tests, use `pytest`:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE.md](./LICENSE) file for details.

## Acknowledgments

- This project is inspired by the historical Enigma machine used during World War II.
- The Bombe simulation pays tribute to the work of Alan Turing and his team at Bletchley Park.

## Resources

- [Enigma Machine - Wikipedia](https://en.wikipedia.org/wiki/Enigma_machine)
- [Bletchley Park](https://bletchleypark.org.uk/)

---

**Project maintained by [Luca Dumitru](https://github.com/luckasz02)**
