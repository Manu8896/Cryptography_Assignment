import string
def affine_encrpt(plain_text,a,b):
    alphabet = string.ascii_uppercase
    encrpted_text=""
    for char in plain_text:
        if char in alphabet:
            index=alphabet.index(char)
            encrpted_index=(a*index+b)%26
            encrpted_char=alphabet[encrpted_index]
            encrpted_text+=encrpted_char
        else:
            encrpted_text+=char
    return encrpted_text
def affine_decrypt(cipher_text,a,b):
    alphabet=string.ascii_uppercase
    decrypted_text=""
    a_inverse=0
    for i in range(26):
        if (a*i)%26==1:
            a_inverse=i
            break
    for char in cipher_text:
        if char in alphabet:
            index=alphabet.index(char)
            decrypted_index=(a_inverse*(index-b))%26
            decrypted_char=alphabet[decrypted_index]
            decrypted_text+=decrypted_char
        else:
            decrypted_text+=char
    return decrypted_text
plain_text=input("Enter the Plain text : ")
a=int(input("Enter the multiplicative value : "))
b=int(input("Enter the additive value : "))
encrypted_text=affine_encrpt(plain_text,a,b)
print("Encrypted text :",encrypted_text)
decrypted_text=affine_decrypt(encrypted_text,a,b)
print("Decrypted text :",decrypted_text)
