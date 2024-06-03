import unittest
from enigma.enigma_machine import EnigmaMachine

class TestEnigmaMachine(unittest.TestCase):
    def setUp(self):
        rotors = [
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ]
        reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        plugboard = {"A": "B", "B": "A"}
        self.enigma = EnigmaMachine(rotors, reflector, plugboard)

    def test_encode_message(self):
        encoded_message = self.enigma.encode_message("HELLO")
        self.assertNotEqual(encoded_message, "HELLO")
        self.assertEqual(len(encoded_message), 5)

if __name__ == '__main__':
    unittest.main()