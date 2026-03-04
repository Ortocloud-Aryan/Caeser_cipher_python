alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]


def caeser(message, shift_amount, direction):
    new_word = ""

    if direction == "decode":
        shift_amount = -shift_amount 

    for letter in message:
        if letter in alphabets:
            index = alphabets.index(letter)
            new_index = (index + shift_amount) % len(alphabets)
            new_word += alphabets[new_index]
        else:
            # keep spaces, numbers, symbols unchanged
            new_word += letter

    print(f"the {direction}d message is as follows : {new_word}")

should_continue = True

while should_continue:
    direction = input("type 'encode' to encrypt the text OR type 'decode' to decrypt the text : \n").strip().lower()
    message = input(f"the text you want to {direction} :\n").strip().lower()
    shift_amount = int((input("The shift number? :\n")).strip())

    caeser(message, shift_amount, direction)

    restart = input("do you want to go again, please type 'yes' to go again or 'no' to stop\n").strip().lower()
    if restart == "no":
        should_continue = False
        print("thank you for using Caeser cipher!")
        

# #Encrypting the message: 
# def encrypt():
#     message = input("Type the message you want to encrypt:\n").lower()
#     shift_amount = int(input("Type the shift number:\n"))
    
#     new_word = ""

#     for letter in message:
#         if letter in alphabets:
#             index = alphabets.index(letter)
#             new_index = (index + shift_amount) % len(alphabets)
#             new_word += alphabets[new_index]
#         else:
#             # keep spaces, numbers, symbols unchanged
#             new_word += letter

#     print("Encrypted message:", new_word)

# #Decrypting the message:
# def decrypt():
#     message = input("type the message you want to decrypt:\n").lower()
#     shift_amount = int(input("Type the shift number:\n"))

#     new_word = ""

#     for letter in message:
#         if letter in alphabets:
#             index = alphabets.index(letter)
#             new_index = (index - shift_amount) % len(alphabets)
#             new_word = new_word + alphabets[new_index]
#         else:
#             #keep spaces, numbers, symbols unchanged
#             new_word = new_word + letter
#     print("Decrypted message :", new_word)



