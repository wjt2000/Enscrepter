encrypt_dict = {
    "x" : "a",
    "y" : "b",
    "z" : "c",
    "X" : "A",
    "Y" : "B",
    "Z" : "C"
    }


# move alphabet
def shift_character(in_character):
    return chr(ord(in_character) + 3)

# encrypt program
def encrypt_caesar(input_string):
    encrypted = ""
    for character in input_string:
        # check if alphabet yes or no
        if character.isalpha():
            if character in encrypt_dict.keys():
                encrypted = encrypted + encrypt_dict[character]
            else:
                encrypted = encrypted + shift_character(character)
                 #space, comma, stay same
        else:
             encrypted = encrypted + character
    return encrypted


mystring = input ("PLEASE ENTER A SENTENCE\n")
encrypted = encrypt_caesar (mystring)
print ("After Encrypt: {0}".format(encrypted))

