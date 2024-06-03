from enigma.enigma_machine import EnigmaMachine
from bombe.bombe import bombe_attack

# Example setup
rotors = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Rotor III
]
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  # Reflector B
plugboard = {"A": "B", "B": "A"}  # Simple plugboard example

enigma = EnigmaMachine(rotors, reflector, plugboard)

# Change this message to whatever you want to test
message = "YOUR MESSAGE"

# Set initial rotor positions for encoding
initial_positions = [0, 0, 0]
enigma.rotor_positions = initial_positions.copy()
encoded_message = enigma.encode_message(message)
print(f"Encoded Message: {encoded_message}")

# Reset rotor positions for decoding
enigma.rotor_positions = initial_positions.copy()
decoded_message = enigma.encode_message(encoded_message)
print(f"Decoded Message: {decoded_message}")

# Ensure decoding works with Bombe
known_plaintext = message
ciphertext = encoded_message

result = bombe_attack(enigma, ciphertext, known_plaintext)
if result:
    positions, decoded_message = result
    print(f"Rotor positions: {positions}")
    print(f"Decoded Message: {decoded_message}")
else:
    print("No valid settings found.")
