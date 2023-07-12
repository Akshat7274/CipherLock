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
    inc = 1
    for i in txt:
        for j in range(ky):
            if (j==ctr):
                mat[j].append(i)
            else:
                mat[j].append("")
        if (ctr==(ky-1)):
            inc = -1
        elif (ctr==0):
            inc = 1
        ctr += inc
    print(tabulate(mat,tablefmt="fancy_grid"))

    for i in mat:
        for j in i:
            if (j!=""):
                ret += j
    return ret

def decrypt(txt,ky):
    print("\n----------------------------------------------------Decryption Process----------------------------------------------------\n")
    print("Ciphertext:",txt)
    print("\nTransposition Matrix:")
    mat = []
    for i in range(ky):
        temp = [""]*len(txt)
        mat.append(temp)
    rail = 0
    pos = rail
    it = 0
    while(it<len(txt)):
        flip = 0
        if (rail==(ky-1)):
            flip = 1
        while (pos<len(txt)):
            mat[rail][pos] = txt[it]
            it += 1
            if (flip==0 and rail!=(ky-1)):
                pos += (((ky - 1) - rail) * 2)
                if (rail>0 and rail<(ky-1)):
                    flip = 1
            elif (flip==1 and rail!=0):
                pos += (rail * 2)
                if (rail>0 and rail<(ky-1)):
                    flip = 0
        rail += 1
        pos = rail

    print(tabulate(mat,tablefmt="fancy_grid"))
    ret = ""
    for i in range(len(txt)):
        for j in range(ky):
            if (mat[j][i]!=""):
                ret += mat[j][i]
    return ret
