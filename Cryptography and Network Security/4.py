# Python3 code to implement Hill Cipher

# Create a 3x3 key matrix initialized with zeros
keyMatrix = [[0] * 3 for i in range(3)]

# Create a vector for the message
messageVector = [[0] for i in range(3)]

# Create a vector for the cipher
cipherMatrix = [[0] for i in range(3)]

# Function to generate the key matrix for the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65  # Map character to an integer in the range 0-25
            k += 1

# Function to encrypt the message using the key matrix
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26  # Apply modulo 26 to get the cipher letter

# Function to perform the Hill Cipher encryption
def HillCipher(message, key):

    # Ensure the message length is 3
    if len(message) != 3:
        raise ValueError("Message length must be 3 for this implementation.")

    # Get the key matrix from the key string
    getKeyMatrix(key)

    # Convert the message into a vector of numbers (A=0, B=1, ..., Z=25)
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    # Encrypt the message using the key matrix
    encrypt(messageVector)

    # Generate the encrypted text from the cipher matrix
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))  # Convert number back to character

    # Print the ciphertext
    print("Ciphertext: ", "".join(CipherText))


# Driver code
def main():
    # Get the message to be encrypted
    message = "ASH"  # You can change this message
    print("Input message:", message)

    # Get the key
    key = "ASHIKRAHM"  # You can change the key
    print("Key:", key)

    # Perform Hill Cipher encryption
    HillCipher(message, key)

if __name__ == "__main__":
    main()
