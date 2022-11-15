# The cipher changes the letter by shifting through the alphabet by the instructed number of shifs

# Receive the message to encrypt
message = input("Enter the message: ")

# The number of characters to shift
key = int(input("How many characters do you want to shft(1-26): "))

# Prepare the secret message
secret_message = ""

# Cycle through each character in the message
for character in message:

    # If it isn't a letter keep it as it is
    if character.isalpha():
        # Else get the character code for the letter and the shift amount
        character_code = ord(character)
        character_code += key

        # If character is uppercase compare it to the uppercase unicodes
        if character.isupper():

            # When key is added if the character code is bigger than 26 subtract 26
            if character_code > ord('Z'):
                character_code -= 26

            # when a key is added if the character code is less than 26 add 26
            if character_code < ord('A'):
                character_code += 26
        # Do the same process for lowercase characters
        else:
            if character_code > ord('z'):
                character_code -= 26
            if character_code < ord('a'):
                character_code += 26
        #  Concert from code to Caesar cipher letters and add to the message
        secret_message += chr(character_code)

        # But for characters that weren't letters and stayed the same
    else:
        secret_message += character

# Now everything has been encrypted
print("Encrypted message is :", secret_message)

# To decrypt we need the negative of key
key = -key

# We copy the entire encryption code
# Change all the secret message to original to get the decrypted message
original_message = ""

# Cycle through each character in the message
for character in secret_message:

    # If it isn't a letter keep it as it is
    if character.isalpha():
        # Else get the character code for the letter and the shift amount
        character_code = ord(character)
        character_code += key

        # If character is uppercase compare it to the uppercase unicodes
        if character.isupper():

            # When key is added if the character code is bigger than 26 subtract 26
            if character_code > ord('Z'):
                character_code -= 26

            # when a key is added if the character code is less than 26 add 26
            if character_code < ord('A'):
                character_code += 26
        # Do the same process for lowercase characters
        else:
            if character_code > ord('z'):
                character_code -= 26
            if character_code < ord('a'):
                character_code += 26
        #  Concert from code to Caesar cipher letters and add to the message
        original_message += chr(character_code)

        # But for characters that weren't letters and stayed the same
    else:
        original_message += character

# Now everything has been encrypted
print("Decrypted message is :", original_message)
