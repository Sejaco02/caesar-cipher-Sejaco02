# establish alphabet and cipher lists to be looped to create dictionary
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher =   ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e']
cipher_dictionary = {}

# Populate cipher dictionary
for letter in alphabet :
    cipher_dictionary[letter] = cipher[alphabet.index(letter)]

# Request Input for word/sentence to cipher and setup output field
translate_me = input("Please enter statement to be encrypted? ")
encryption = str()

# run encryption and print output
for char in translate_me:
    if char.isupper():
        encryption += ((cipher_dictionary.get(char.lower(),char))).upper()
    else:
       encryption += (cipher_dictionary.get(char.lower(),char))

print("Encrypted statement:", encryption)