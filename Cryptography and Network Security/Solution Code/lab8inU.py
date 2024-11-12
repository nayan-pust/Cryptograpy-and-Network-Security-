import string

# Define alphabet mappings
alphabetic = string.ascii_lowercase
mp = dict(zip(alphabetic, range(26)))
mp2 = dict(zip(range(26), alphabetic))

# Function to generate the repeating key
def generateKey(message, key):
    key_word = ""
    for i in range(len(message)):
        key_word += key[i % len(key)]
    return key_word

# Decryption function
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        decrypted_message += mp2[(mp[encrypted_message[i]] - mp[key[i]] + 26) % 26]
    return decrypted_message

# Get user inputs for encrypted message and key
encrypted_message = input("Enter the encrypted message: ").lower().replace(" ", "")
key_input = input("Enter the decryption key: ").lower().replace(" ", "")

# Generate the repeated key based on encrypted message length
key = generateKey(encrypted_message, key_input)

# Perform decryption
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted Message:", decrypted_message)
