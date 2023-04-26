# al="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# list=[]
# for i in al:
#     list.append(i)
# print(list)
text=[' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def encrypt(plaintext,shift_amount):
    cipher_letter=""
    for letter in plaintext:
        position=text.index(letter)
        new_position=position+shift_amount
        new_letter=text[new_position]
        cipher_letter+=new_letter
    print(cipher_letter)


def decrypt(plaintext,shift_amount):
    cipher_letter=""
    for letter in plaintext:
        position=text.index(letter)
        new_position=position-shift_amount
        new_letter=text[new_position]
        cipher_letter+=new_letter
    print(cipher_letter)
 

direction=input("Type 'encode' for encryption and 'decode' for decryption")
text_n=input("Type your message\n").lower()
shift=int(input("Type the shift amount\n"))

if direction =="encode":

    encrypt(text_n,shift)

else:
     decrypt(text_n,shift)