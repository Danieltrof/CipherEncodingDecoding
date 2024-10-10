import os
import nltk
from nltk.corpus import words

# Download the word list (if not already done)
nltk.download('words')

# Standard English alphabet
ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ENGLISH_WORDS = set(words.words())

def caesar_brute_force(cipher_text):
    # Display the cipher message being cracked
    print(f"\nTrying to crack the cipher message: {cipher_text}\n")
    
    # Loop through all possible shifts (1 to 25 for the English alphabet)
    for shift in range(1, len(ENGLISH_ALPHABET)):
        decrypted_text = ''
        
        # Try decrypting by shifting each letter in the cipher text
        for char in cipher_text:
            if char.lower() in ENGLISH_ALPHABET:  # Only shift alphabetic characters
                shifted_index = (ENGLISH_ALPHABET.index(char.lower()) - shift) % len(ENGLISH_ALPHABET)
                new_char = ENGLISH_ALPHABET[shifted_index]
                
                # Preserve case (upper or lower)
                if char.isupper():
                    decrypted_text += new_char.upper()
                else:
                    decrypted_text += new_char
            else:
                decrypted_text += char  # Non-alphabetic characters remain unchanged
        
        # Check if the decrypted text contains meaningful words
        if is_meaningful(decrypted_text):
            if shift == 3:
                print(f"Shift {shift} (Standard Caesar Cipher): {decrypted_text}")
            else:
                print(f"Shift {shift}: {decrypted_text}")

# Function to check if a text contains meaningful words
def is_meaningful(text):
    words_in_text = text.split()
    valid_words = [word for word in words_in_text if word.lower() in ENGLISH_WORDS]
    
    # Consider meaningful if more than half of the words are valid
    return len(valid_words) / len(words_in_text) > 0.5 if words_in_text else False

# Get input from the user
def get_cipher_text():
    choice = input("Would you like to enter the cipher text manually or provide a file? (enter/file): ").strip().lower()
    
    if choice == 'enter':
        return input("Enter the cipher text: ").strip()
    elif choice == 'file':
        file_path = input("Enter the file path: ").strip()
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                return file.read().strip()
        else:
            print("File not found.")
            return None
    else:
        print("Invalid choice.")
        return None

# Main script execution
cipher_text = get_cipher_text()

if cipher_text:
    caesar_brute_force(cipher_text)
else:
    print("No valid input provided.")
