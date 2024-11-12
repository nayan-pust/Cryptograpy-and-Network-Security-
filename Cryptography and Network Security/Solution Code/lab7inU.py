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

# Encryption function
def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_message += mp2[(mp[message[i]] + mp[key[i]]) % 26]
    return encrypted_message

# Get user inputs for message and key
message = input("Enter the message to encrypt: ").lower().replace(" ", "")
key_input = input("Enter the encryption key: ").lower().replace(" ", "")

# Generate the repeated key based on message length
key = generateKey(message, key_input)

# Perform encryption
encrypted_message = encrypt(message, key)
print("Encrypted Message:", encrypted_message)
