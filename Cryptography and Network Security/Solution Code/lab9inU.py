# encryption_script.py

def stringEncryption(text, key):
    cipherText = ""
    cipher = []

    # Generate cipher values
    for i in range(len(key)):
        cipher.append(ord(text[i]) - ord('A') + ord(key[i]) - ord('A'))

    # Adjust values to fit within the alphabet range
    for i in range(len(key)):
        if cipher[i] > 25:
            cipher[i] = cipher[i] - 26

    # Convert numeric cipher values back to characters
    for i in range(len(key)):
        x = cipher[i] + ord('A')
        cipherText += chr(x)

    return cipherText

# Get user input for plain text and key
plainText = input("Enter the plain text: ").upper().replace(" ", "")
key = input("Enter the encryption key: ").upper().replace(" ", "")

# Check if the key length matches the text length
if len(key) != len(plainText):
    print("Error: The key must be the same length as the plain text.")
else:
    # Encrypt the text
    encryptedText = stringEncryption(plainText, key)
    print("Cipher Text - " + encryptedText)
