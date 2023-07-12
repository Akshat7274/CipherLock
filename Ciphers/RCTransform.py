# Row Column Transformation Cipher Implementation

from tabulate import tabulate

def encrypt(txt,ky):
    print("\n----------------------------------------------------Encryption Process----------------------------------------------------\n")
    key_arr = ky.split(" ")
    nc = len(key_arr)
    mat = []
    temp = []
    ct = 0
    while (ct<len(txt)):
        temp.append(txt[ct])
        ct += 1
        if (ct%nc==0):
            mat.append(temp)
            temp = []
        elif (ct==len(txt)):
            while (len(temp)!=nc):
                temp.append("")
            mat.append(temp)
    print("Plaintext: ",txt)
    print("\nTransposition Matrix: ")
    print(tabulate(mat,tablefmt="grid"))
    
    ret = ""
    for i in key_arr:
        for j in range(len(mat)):
            ret += mat[j][int(i)-1]
    return ret

def decrypt(txt,ky):
    print("\n----------------------------------------------------Decryption Process----------------------------------------------------\n")
    key_arr = ky.split(" ")
    nc = len(key_arr)
    if (len(txt)%nc==0):
        nr = len(txt) // nc
    else:
        nr = len(txt) // nc + 1
    mat = []
    for i in range(nr):
        temp = []
        for j in range(nc):
            temp.append("")
        mat.append(temp)
    i = 0
    curr = 0
    while (i<len(txt)):
        k = int(key_arr[curr])
        if (k>len(txt)%nc and len(txt)%nc!=0):
            ne = nr - 1
        else:
            ne = nr
        row = 0
        for x in range(ne):
            mat[row][k-1] = txt[i+x]
            row += 1
        i += x + 1
        curr += 1
    print("Ciphertext: ",txt)
    print("\nTransposition Matrix: ")
    print(tabulate(mat,tablefmt="grid"))

    ret = ""
    for i in mat:
        for j in i:
            if (j!=""):
                ret += j
    return ret