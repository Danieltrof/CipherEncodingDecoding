import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, mode):
    result = []
    for char in text:
        if char.isalpha():
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift * mode) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift * mode) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def encrypt_text():
    plaintext = input_text.get("1.0", "end-1c")
    shift = int(shift_var.get())
    ciphertext = caesar_cipher(plaintext, shift, 1)  # Mode 1 for encryption
    output_text.delete("1.0", "end")
    output_text.insert("1.0", ciphertext)

def decrypt_text():
    ciphertext = input_text.get("1.0", "end-1c")
    shift = int(shift_var.get())
    plaintext = caesar_cipher(ciphertext, shift, -1)  # Mode -1 for decryption
    output_text.delete("1.0", "end")
    output_text.insert("1.0", plaintext)

# Create GUI
root = tk.Tk()
root.title("Caesar Cipher Decoder/Encoder")

# Input
input_label = ttk.Label(root, text="Input Text:")
input_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

input_text = tk.Text(root, height=5, width=50)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Shift
shift_label = ttk.Label(root, text="Shift Amount:")
shift_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

shift_var = tk.StringVar()
shift_entry = ttk.Entry(root, textvariable=shift_var, width=10)
shift_entry.grid(row=2, column=1, padx=10, pady=10)

# Output
output_label = ttk.Label(root, text="Output Text:")
output_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

#Buttons
encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=5, column=0, padx=10, pady=10)

decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=5, column=1, padx=10, pady=10)

# Start the GUI
root.mainloop()
