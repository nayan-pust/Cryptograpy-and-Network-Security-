def brute_force_decrypt(ciphertext):
    print("\nAttempting all possible decryption shifts:")
    print("-" * 50)
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift:2d}: {decrypted_text}")


def brute_force_encrypt(plainText):
    print("\nGenerating all possible encryption shifts:")
    print("-" * 50)
    for shift in range(26):
        encrypted_text = caesar_encrypt(plainText, shift)
        print(f"Shift {shift:2d}: {encrypted_text}")


def caesar_encrypt(plainText, shift):
    encrypted_text = ""
    for char in plainText:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Apply shift and wrap around using modulo
            shifted = (ord(char) - ascii_base + shift) % 26
            encrypted_text += chr(ascii_base + shifted)
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Apply reverse shift and wrap around using modulo
            shifted = (ord(char) - ascii_base - shift) % 26
            decrypted_text += chr(ascii_base + shifted)
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_text += char
    return decrypted_text


def main():
    # Test the implementation
    plaintext = input("Enter the text to encrypt: ")
    
    print("\n=== ENCRYPTION RESULTS ===")
    print(f"Original text: {plaintext}")
    brute_force_encrypt(plaintext)
    
    # For testing decryption, we'll use shift 1 as an example
    ciphertext = caesar_encrypt(plaintext, 1)
    print("\n=== DECRYPTION RESULTS ===")
    print(f"Encrypted text (shift 1): {ciphertext}")
    brute_force_decrypt(ciphertext)


if __name__ == "__main__":
    main()