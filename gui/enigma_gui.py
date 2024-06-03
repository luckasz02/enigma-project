import sys
import os
import tkinter as tk
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enigma.enigma_machine import EnigmaMachine

class EnigmaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Enigma Machine Simulator")

        self.label_input = tk.Label(master, text="Input Message:")
        self.label_input.pack()

        self.entry_input = tk.Entry(master)
        self.entry_input.pack()

        self.label_output = tk.Label(master, text="Encoded/Decoded Message:")
        self.label_output.pack()

        self.text_output = tk.Text(master, height=5, width=50)
        self.text_output.pack()

        self.button_encode = tk.Button(master, text="Encode", command=self.encode_message)
        self.button_encode.pack()

        self.button_decode = tk.Button(master, text="Decode", command=self.decode_message)
        self.button_decode.pack()

        rotors = [
            'JGDQOXUSCAMIFRVTPNEWKBLZYH',
            'NTZPSFBOKMWRCJDIVLAEYUXHGQ', 
            'JVIUBHTCDYAKEQZPOSGXNRMWFL'  
        ]
        reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        plugboard = {'A': 'B', 'B': 'A'}  
 

        self.enigma_machine = EnigmaMachine(rotors, reflector, plugboard)

    def encode_message(self):
        self.enigma_machine.reset_rotor_positions()
        input_text = self.entry_input.get()
        encoded_message = self.enigma_machine.encode_message(input_text)
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, encoded_message)

    def decode_message(self):
        self.enigma_machine.reset_rotor_positions()
        input_text = self.entry_input.get()
        decoded_message = self.enigma_machine.encode_message(input_text)
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, decoded_message)

if __name__ == "__main__":
    root = tk.Tk()
    gui = EnigmaGUI(root)
    root.mainloop()
