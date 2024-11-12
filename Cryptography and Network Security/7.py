# Encryption Program
def generate_key_encrypt(message, key):
    """Extend the key to match the message length for encryption"""
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encryption():
    """Encrypt a message using Poly-Alphabetic cipher"""
    message = input("Enter message to encrypt: ")
    key = input("Enter key: ")
    
    # Generate the key
    key = generate_key_encrypt(message, key)
    cipher_text = []
    
    # Perform encryption
    for i in range(len(message)):
        if message[i].isalpha():
            # Handle uppercase letters
            if message[i].isupper():
                value = (ord(message[i]) + ord(key[i].upper()) - 2 * ord('A')) % 26
                cipher_text.append(chr(value + ord('A')))
            # Handle lowercase letters
            else:
                value = (ord(message[i]) + ord(key[i].lower()) - 2 * ord('a')) % 26
                cipher_text.append(chr(value + ord('a')))
        # Keep non-alphabetic characters as they are
        else:
            cipher_text.append(message[i])
            
    encrypted_text = "".join(cipher_text)
    print(f"\nEncrypted Message: {encrypted_text}")

if __name__ == "__main__":
    print("Poly-Alphabetic Cipher Encryption")
    print("--------------------------------")
    encryption()