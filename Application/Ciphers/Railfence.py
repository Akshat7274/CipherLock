# Railfence Cipher Implementation

from tabulate import tabulate

def encrypt(txt,ky):
    print("\n----------------------------------------------------Encryption Process----------------------------------------------------\n")
    print("Plaintext:",txt)
    print("\nTransposition Matrix:")
    mat = []
    ret = ""
    for i in range(ky):
        mat.append([])
    ctr = 0
    for i in txt:
        mat[ctr%ky].append(i)
        ctr += 1
    print(tabulate(mat,tablefmt="fancy_grid"))
    for i in mat:
        for j in i:
            ret += j
    return ret

def decrypt(txt,ky):
    print("\n----------------------------------------------------Decryption Process----------------------------------------------------\n")
    print("Ciphertext:",txt)
    mat = []
    ret = ""
    for i in range(ky):
        mat.append([])
    ctr = 0
    rc = 0
    nor = 0
    cr = 0
    l = len(txt) % ky
    if (l==0):
        nor = len(txt) // ky
    else:
        nor = len(txt) // ky + 1
    i = 0
    while (True):
        if (rc%nor==nor-1):
            if (ctr<l):
                mat[cr].append(txt[i])
                ctr += 1
            else:
                txt = txt[:i] + " " + txt[i:]
            cr += 1
        else:
            mat[cr].append(txt[i])
        rc += 1
        i += 1
        print(i,len(txt))
        if (i==len(txt)):
            break
    print("\nTransposition Matrix:")
    print(tabulate(mat,tablefmt="fancy_grid"))
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            if (len(mat[j])==i):
                break
            else:
                ret += mat[j][i]
    return ret