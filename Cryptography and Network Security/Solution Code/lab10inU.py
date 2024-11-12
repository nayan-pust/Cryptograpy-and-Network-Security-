def stringDecryption(s, key):
    plainText = ""
    plain = []

    # Convert both ciphertext and key to uppercase for consistency
    s = s.upper()
    key = key.upper()

    for i in range(len(key)):
        # Subtract corresponding character values (uppercase)
        plain.append(ord(s[i]) - ord('A') - (ord(key[i]) - ord('A')))

    for i in range(len(key)):
        if plain[i] < 0:
            plain[i] = plain[i] + 26

    for i in range(len(key)):
        x = plain[i] + ord('A')
        plainText += chr(x)

    return plainText

# Get user input for cipher text and key
cipherText = input("Enter the cipher text to decrypt: ").upper().replace(" ", "")
key = input("Enter the decryption key: ").upper().replace(" ", "")

# Decrypt the message
decryptedText = stringDecryption(cipherText, key)
print("Decrypted Message - " + decryptedText)