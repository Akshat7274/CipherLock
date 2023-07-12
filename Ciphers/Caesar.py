# Caesar Cipher Implementation

def encrypt(tx,s):
    j = ""
    for i in tx:
        if i.islower():
            j += chr(((ord(i) - 97 + s) % 26) + 97)
        elif i.isupper():
            j += chr(((ord(i) - 65 + s) % 26) + 65)
        elif i.isnumeric():
            j += chr(((ord(i) - 48 + s) % 10) + 48)
        else:
            j += i
    return j

def decrypt(tx,s):
    j = ""
    for i in tx:
        if i.islower():
            j += chr(((ord(i) - 97 - s) % 26) + 97)
        elif i.isupper():
            j += chr(((ord(i) - 65 - s) % 26) + 65)
        elif i.isnumeric():
            j += chr(((ord(i) - 48 - s) % 10) + 48)
        else:
            j += i
    return j