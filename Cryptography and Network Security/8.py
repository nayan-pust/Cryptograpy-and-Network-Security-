# Decryption Program
def generate_key_decrypt(cipher_text, key):
    """Extend the key to match the cipher text length for decryption"""
    key = list(key)
    if len(cipher_text) == len(key):
        return key
    else:
        for i in range(len(cipher_text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def decryption():
    """Decrypt a message using Poly-Alphabetic cipher"""
    cipher_text = input("Enter message to decrypt: ")
    key = input("Enter key: ")
    
    # Generate the key
    key = generate_key_decrypt(cipher_text, key)
    plain_text = []
    
    # Perform decryption
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            # Handle uppercase letters
            if cipher_text[i].isupper():
                value = (ord(cipher_text[i]) - ord(key[i].upper()) + 26) % 26
                plain_text.append(chr(value + ord('A')))
            # Handle lowercase letters
            else:
                value = (ord(cipher_text[i]) - ord(key[i].lower()) + 26) % 26
                plain_text.append(chr(value + ord('a')))
        # Keep non-alphabetic characters as they are
        else:
            plain_text.append(cipher_text[i])
            
    decrypted_text = "".join(plain_text)
    print(f"\nDecrypted Message: {decrypted_text}")

if __name__ == "__main__":
    print("Poly-Alphabetic Cipher Decryption")
    print("--------------------------------")
    decryption()