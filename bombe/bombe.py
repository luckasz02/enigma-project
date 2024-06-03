from itertools import product
from copy import deepcopy
from enigma.enigma_machine import EnigmaMachine

def create_enigma_copy(original_enigma):
    return EnigmaMachine(
        rotors=deepcopy(original_enigma.rotors),
        reflector=deepcopy(original_enigma.reflector),
        plugboard=deepcopy(original_enigma.plugboard)
    )

def decode_with_settings(enigma, settings, ciphertext):
    enigma.rotor_positions = list(settings)
    return enigma.encode_message(ciphertext)

def bombe_attack(enigma, ciphertext, known_plaintext):
    for positions in product(range(26), repeat=len(enigma.rotors)):
        test_enigma = create_enigma_copy(enigma)
        decoded_message = decode_with_settings(test_enigma, positions, ciphertext)
        print(f"Trying positions: {positions} -> Decoded message: {decoded_message} (Expected: {known_plaintext})")
        if known_plaintext in decoded_message:
            print(f"Found positions: {positions} with decoded message: {decoded_message}")
            return positions, decoded_message
    return None
