import string

# Create alphabet mappings
alphabet = string.ascii_lowercase
mp = dict(zip(alphabet, range(26)))
mp2 = dict(zip(range(26), alphabet))

# Caesar encryption function
def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char in mp:  # Encrypt only if character is in the alphabet
            encrypted_message += mp2[(mp[char] + shift) % 26]
        else:
            encrypted_message += char  # Leave spaces and other characters unchanged
    return encrypted_message

# Brute force decryption function
def bruteforce_decrypt(encrypted_message):
    decrypted_messages = []
    for i in range(26):
        decryp = ""
        for char in encrypted_message:
            if char in mp:  # Decrypt only if character is in the alphabet
                decryp += mp2[(mp[char] - i + 26) % 26]
            else:
                decryp += char  # Leave spaces and other characters unchanged
        decrypted_messages.append(decryp)
    return decrypted_messages

# Input message and shift
message = "hello world hi naima"
shift = 7
encrypted_message = caesar_encrypt(message, shift)
decrypted_messages = bruteforce_decrypt(encrypted_message)

# Output the results
print("Encrypted Message:", encrypted_message)
print("Decrypted Messages:")
for ind, msg in enumerate(decrypted_messages):
    print(f"For key {ind}: {msg}")
