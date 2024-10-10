def generate_vigenere_table():
    table = []
    for i in range(26):
        row = [(chr((i + j) % 26 + 65)) for j in range(26)]
        table.append(row)
    return table

def format_string(s):
    return ''.join([c.upper() for c in s if c.isalpha()])

def vigenere_encrypt(plaintext, key, table):
    plaintext = format_string(plaintext)
    key = format_string(key)
    
    encrypted = []
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        row = ord(char) - 65
        col = ord(key[i % key_length]) - 65
        encrypted.append(table[row][col])
    
    return ''.join(encrypted)

def vigenere_decrypt(ciphertext, key, table):
    ciphertext = format_string(ciphertext)
    key = format_string(key)
    
    decrypted = []
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        col = ord(key[i % key_length]) - 65
        row = [r[col] for r in table].index(char)
        decrypted.append(chr(row + 65))
    
    return ''.join(decrypted)

def main():
    table = generate_vigenere_table()
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    text = input("Enter the text: ")
    key = input("Enter the key: ")

    if choice == 'E':
        encrypted = vigenere_encrypt(text, key, table)
        print("Encrypted text:", encrypted)
    elif choice == 'D':
        decrypted = vigenere_decrypt(text, key, table)
        print("Decrypted text:", decrypted)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
