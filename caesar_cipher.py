#EH p1 ceasar cipher

# PSEUDOCODE YABA DAB DOOOOO:
# Ask the user if they want to encode or decode
# Ask the user for the message OU YAH
# Ask the user for the shift number
# If user says encode: call the encode function and show the result
# If usar says decode: call the decode function and show the result

def encode(message, shift):
    # PSEUDOCODE for ENCODE OUUUUUUUUUUUUUUUUUUUUUUUU YAH:
    # Start with an empty string
    # Look at each letter one by one
    # If it is a letter, move it forward by the shift amount
    # If it goes past Z or z, wrap back to the beginning
    # If it is not a letter (space, number, etc.), leave it alone
    # Return the new message
    
    result = ""
    
    for char in message:
        if char.isalpha():
            if char.isupper():
                # Uppercase letter
                new_charmander = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Lowercase letter
                new_charmander = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result = result + new_charmander
        else:
            # Not a letter, keep it the same
            result = result + char
            
    return result


def decode(message, shift):
    # PSEUDOCODE for decode WAASAAAA:
    # Decoding is the same as encoding but we go backwards IS THE SAME WWOOOAAAh
    # So we just call encode with a negative shift
    
    return encode(message, -shift)


def main():
    print("***CEASAR CIPHER GAME MUAJAJAJAJAJA***")
    print()
    
    # Ask if the user wants to encode or decode
    choice = input("Type E to encode or D to decode: ")
    choice = choice.upper()
    
    # Ask for the message
    message = input("Enter your message HERE please: ")
    
    # Ask for the shift value
    shift = int(input("Enter the shift number Aqui WASAAAaa: "))
    
    print()
    
    # Check what the user chose and call the right function
    if choice == "E":
        result = encode(message, shift)
        print("Encoded message:", result)
    else:
        result = decode(message, shift)
        print("Decoded message:", result)


# Start the program OWOWOOMsinf ennfienudfuenfeunddni...Sorry it was really late THANK YA
main()
