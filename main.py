from enigma.enigma_machine import EnigmaMachine
from bombe.bombe import bombe_attack

rotors = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   
]
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  
plugboard = {"A": "B", "B": "A"}  

enigma = EnigmaMachine(rotors, reflector, plugboard)

message = "YOUR MESSAGE"

initial_positions = [0, 0, 0]
enigma.rotor_positions = initial_positions.copy()
encoded_message = enigma.encode_message(message)
print(f"Encoded Message: {encoded_message}")

enigma.rotor_positions = initial_positions.copy()
decoded_message = enigma.encode_message(encoded_message)
print(f"Decoded Message: {decoded_message}")

known_plaintext = message
ciphertext = encoded_message

result = bombe_attack(enigma, ciphertext, known_plaintext)
if result:
    positions, decoded_message = result
    print(f"Rotor positions: {positions}")
    print(f"Decoded Message: {decoded_message}")
else:
    print("No valid settings found.")
