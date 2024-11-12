# Define the normal alphabet and the corresponding coded alphabet
normal_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

coded_char = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O',
              'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
              'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

# Function to encrypt the text
def string_encryption(s):
    encrypted_string = ""

    # Encode each character based on the mapping
    for char in s:
        if char in normal_char:
            # Find the index of the character in normal_char
            index = normal_char.index(char)
            # Use the index to get the corresponding coded character
            encrypted_string += coded_char[index]
        else:
            # Add non-alphabet characters directly
            encrypted_string += char

    return encrypted_string

# Function to decrypt the text
def string_decryption(s):
    decrypted_string = ""

    # Decode each character based on the mapping
    for char in s:
        if char in coded_char:
            # Find the index of the character in coded_char
            index = coded_char.index(char)
            # Use the index to get the corresponding normal character
            decrypted_string += normal_char[index]
        else:
            # Add non-alphabet characters directly
            decrypted_string += char

    return decrypted_string

# Main section to demonstrate encryption and decryption
if __name__ == "__main__":
    plain_text = "noyon"

    # Convert plain text to lowercase for encryption
    print("Plain text:", plain_text)
    encrypted_text = string_encryption(plain_text.lower())

    # Print encrypted text
    print("Encrypted message:", encrypted_text)

    # Decrypt and print the original message
    decrypted_text = string_decryption(encrypted_text)
    print("Decrypted message:", decrypted_text)
