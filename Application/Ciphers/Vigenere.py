# Vigenere Cipher Implementation

from tabulate import tabulate

def key_print():
    print("\n\n---------------------------------------------------------Vigenere Key Table---------------------------------------------------------\n")
    tbl = [[""]]
    for i in range(26):
        tbl[0].append(chr(i+97))
    for i in range(26):
        temp = [chr(i+97)]
        for j in range(26):
            temp.append(chr(((i+j)%26)+97))
        tbl.append(temp)
    print(tabulate(tbl,headers="firstrow"))

def encrypt(txt,ky):
    ret = []
    cnt = 0
    key = ""
    ct = ""
    for i in txt:
        if (i==" "):
            key += " "
            ct += " "
        else:
            key += ky[cnt%len(ky)]
            if i.islower():
                ct += chr(97 + ((ord(i) - 97) + (ord(key[-1]) - 97)) % 26)
            else:
                ct += chr(65 + ((ord(i) - 65) + (ord(key[-1]) - 97)) % 26)
            cnt += 1
    ret.append(["Plaintext:",txt])
    ret.append(["Mapped Key:\t",key])
    ret.append(["Ciphertext:\t",ct])
    return ret

def decrypt(txt,ky):
    ret = []
    cnt = 0
    key = ""
    pt = ""
    for i in txt:
        if (i==" "):
            key += " "
            pt += " "
        else:
            key += ky[cnt%len(ky)]
            if i.islower():
                pt += chr(97 + ((ord(i) - 97) - (ord(key[-1]) - 97)) % 26)
            else:
                pt += chr(65 + ((ord(i) - 65) - (ord(key[-1]) - 97)) % 26)
            cnt += 1
    ret.append(["Ciphertext:",txt])
    ret.append(["Mapped Key:\t",key])
    ret.append(["Plaintext:\t",pt])
    return ret