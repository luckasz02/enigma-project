from copy import deepcopy

class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = deepcopy(rotors)
        self.reflector = deepcopy(reflector)
        self.plugboard = deepcopy(plugboard)
        self.rotor_positions = [0] * len(rotors)

    def encode_character(self, char):
        original_char = char
        if char in self.plugboard:
            char = self.plugboard[char]

        for i, rotor in enumerate(self.rotors):
            index = (ord(char) - 65 + self.rotor_positions[i]) % 26
            char = rotor[index]

        char = self.reflector[ord(char) - 65]

        for i, rotor in enumerate(self.rotors):
            index = (ord(char) - 65 + self.rotor_positions[i]) % 26
            char = rotor[index]
        
        char = self.reflector[ord(char) - 65]
        
        for i, rotor in enumerate(reversed(self.rotors)):
            index = (rotor.index(char) - self.rotor_positions[-1 - i] + 26) % 26
            char = chr(index + 65)

        if char in self.plugboard:
            char = self.plugboard[char]

        self.rotate_rotors()

        print(f"Encoded {original_char} to {char} (Rotor positions: {self.rotor_positions})")
        return char

    def rotate_rotors(self):
        for i in range(len(self.rotors)):
            self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 26
            if self.rotor_positions[i] != 0:
                break

    def encode_message(self, message):
        encoded_message = ""
        for char in message:
            if char.isalpha():
                encoded_message += self.encode_character(char.upper())
            else:
                encoded_message += char
        return encoded_message

    def decode_message(self, message):
        return self.encode_message(message)
    
    def reset_rotor_positions(self):
        self.rotor_positions = [0] * len(self.rotors)
