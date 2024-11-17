# add your code here
# The alphabet to map letters
letters = "abcdefghijklmnopqrstuvwxyz"

# Create a dictionary for encryption with a shift of 5
encryption = {}
for i in range(26): 
    j = (i + 5) % 26  # Shift letters by 5
    encryption[letters[i]] = letters[j]

# Take the secret message as input
secret_sentence = input("Type a secret message: ")

# Print the original message and convert it to lowercase
print("Original Message:", secret_sentence)
secret_sentence = secret_sentence.lower()

# Encrypt the message
encrypted_text = ""
for letter in secret_sentence:
    if letter in encryption:
        encrypted_text += encryption[letter]  # Encrypt the letter
    else:
        encrypted_text += letter  # Keep non-alphabet characters (e.g., spaces, punctuation)

# Output the encrypted message
print("Encrypted Message:", encrypted_text)


secret_sentence: "i love coding in python"
encrypted_text: "n qtja htnsjl ns uduysm" 
