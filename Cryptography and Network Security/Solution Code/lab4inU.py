from sympy import Matrix
from sympy.polys.polyerrors import NotInvertible

# Function to generate the key matrix from a key string
def get_key_matrix(key, size):
    return Matrix(size, size, [ord(char) % 65 for char in key])

# Hill cipher encryption function
def hill_encrypt(message, key):
    message_vector = Matrix([ord(char) % 65 for char in message])
    cipher_vector = (key * message_vector) % 26
    ciphertext = "".join(chr(int(num) + 65) for num in cipher_vector)
    return ciphertext

# Hill cipher decryption function
def hill_decrypt(ciphertext, key):
    try:
        # Check if the key matrix has an inverse under mod 26
        key_inv = key.inv_mod(26)  # Get modular inverse of the key matrix
    except NotInvertible:
        raise ValueError("The key matrix is not invertible under modulo 26. Choose a different key.")
    
    cipher_vector = Matrix([ord(char) % 65 for char in ciphertext])
    message_vector = (key_inv * cipher_vector) % 26
    decrypted_message = "".join(chr(int(num) + 65) for num in message_vector)
    return decrypted_message

# Get user inputs for message, key, and matrix size
size = int(input("Enter the matrix size (e.g., 2 for 2x2 or 3 for 3x3): "))
key = input(f"Enter a {size * size}-character key: ").upper()
message = input(f"Enter the message to encrypt ({size} characters): ").upper()

# Validate that the key and message lengths are correct for the matrix size
if len(key) != size * size:
    print(f"Error: Key must be exactly {size * size} characters long.")
elif len(message) != size:
    print(f"Error: Message must be exactly {size} characters long.")
else:
    # Generate key matrix
    key_matrix = get_key_matrix(key, size)
    
    # Check if the key matrix is invertible before encryption
    try:
        # Encrypt and then decrypt the message
        ciphertext = hill_encrypt(message, key_matrix)
        print("Ciphertext:", ciphertext)

        decrypted_message = hill_decrypt(ciphertext, key_matrix)
        print("Decrypted Message:", decrypted_message)
    except ValueError as e:
        print(e)