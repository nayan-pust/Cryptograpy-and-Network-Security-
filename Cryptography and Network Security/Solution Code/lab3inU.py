import string

# Define alphabet mappings
alphabet = string.ascii_lowercase
mp = dict(zip(alphabet, range(26)))
mp2 = dict(zip(range(26), alphabet))

# Define Caesar encryption function
def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char in mp:  # Ensure only alphabet characters are encrypted
            encrypted_message += mp2[(mp[char] + shift) % 26]
        else:
            encrypted_message += char  # Keep non-alphabet characters as is
    return encrypted_message

# Define brute-force decryption function
def bruteforce_decrypt(encrypted_message):
    decrypted_message = []
    for i in range(26):
        decryp = ""
        for j in range(len(encrypted_message)):
            if encrypted_message[j] in mp:
                decryp += mp2[(mp[encrypted_message[j]] - i + 26) % 26]
            else:
                decryp += encrypted_message[j]
        decrypted_message.append(decryp)
    return decrypted_message

# Get inputs from the user
message = input("Enter the message to encrypt: ").lower()
shift = int(input("Enter the shift value (0-25): "))

# Perform encryption and decryption
encrypted_message = caesar_encrypt(message, shift)
decrypted = bruteforce_decrypt(encrypted_message)

# Display results
print("Encrypted Message:", encrypted_message)
print("Decrypted Messages:")
for key, msg in enumerate(decrypted):
    print(f"For key {key}: {msg}")
