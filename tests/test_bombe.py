import unittest
from enigma.enigma_machine import EnigmaMachine
from bombe.bombe import bombe_attack

class TestBombe(unittest.TestCase):
    def setUp(self):
        rotors = [
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ]
        reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        plugboard = {"A": "B", "B": "A"}
        self.enigma = EnigmaMachine(rotors, reflector, plugboard)
        self.known_plaintext = "HELLO"
        self.ciphertext = self.enigma.encode_message(self.known_plaintext)

    def test_bombe_attack(self):
        result = bombe_attack(self.enigma, self.ciphertext, self.known_plaintext)
        self.assertIsNotNone(result)
        positions, decoded_message = result
        self.assertIn(self.known_plaintext, decoded_message)

if __name__ == '__main__':
    unittest.main()
