#Playfair Cipher Implementation

from tabulate import tabulate

def txtsplit(tx):
    j = ""
    for i in tx:
        if (len(j)==0 or j[-1]==" "):
            j += i
        else:
            if (j[-1]==i):
                j += "X " + i
            else:
                j += i + " "
    j = j.replace("j","I")
    if (j[-1]==" "):
        return j[0:-1]
    else:
        return j+"Z"

def key_matrix(ky):
    j = []
    temp = []
    for i in ky:
        ex = False
        for x in j:
            if (i in x):
                ex = True
        if (not ex and i not in temp):
            temp.append(i)
        if (len(temp)==5):
            j.append(temp)
            temp = []
    for i in range(97,123):
        if (chr(i) not in ky and i!=106):
            temp.append(chr(i))
        if (len(temp)==5):
            j.append(temp)
            temp = []
    return j

def encrypt(spl,mat):
    buff = spl.split(" ")
    enc = ""
    for i in buff:
        fin1 = i[0].lower()
        fin2 = i[1].lower()
        i1 , j1 , i2 , j2 = 0 , 0 , 0 , 0
        for x in range(len(mat)):
            for y in range(len(mat[x])):
                if (mat[x][y]==fin1):
                    i1 = x
                    j1 = y
                if (mat[x][y]==fin2):
                    i2 = x
                    j2 = y
        if (i1==i2):
            enc += mat[i1][(j1+1)%5] + mat[i2][(j2+1)%5]
        elif (j1==j2):
            enc += mat[(i1+1)%5][j1] + mat[(i2+1)%5][j2]
        else:
            enc += mat[i1][j2] + mat[i2][j1]

        if (i[0].isupper()):
            enc = enc[0:-2] + enc[-2].upper() + enc[-1]
        if (i[1].isupper()):
            enc = enc[0:-1] + enc[-1].upper()
    return enc

def decrypt(spl,mat):
    print(spl)
    buff = []
    temp = ""
    for x in spl:
        temp += x
        if (len(temp)==2):
            buff.append(temp)
            temp = ""
    dec = ""
    for i in buff:
        fin1 = i[0].lower()
        fin2 = i[1].lower()
        i1 , j1 , i2 , j2 = 0 , 0 , 0 , 0
        for x in range(len(mat)):
            for y in range(len(mat[x])):
                if (mat[x][y]==fin1):
                    i1 = x
                    j1 = y
                if (mat[x][y]==fin2):
                    i2 = x
                    j2 = y
        if (i1==i2):
            dec += mat[i1][(j1-1)%5] + mat[i2][(j2-1)%5] + " "
        elif (j1==j2):
            dec += mat[(i1-1)%5][j1] + mat[(i2-1)%5][j2] + " "
        else:
            dec += mat[i1][j2] + mat[i2][j1] + " "

        if (i[0].isupper()):
            dec = dec[0:-3] + dec[-3].upper() + dec[-2:]
        if (i[1].isupper()):
            dec = dec[0:-2] + dec[-2].upper() + dec[-1]
    return dec[0:-1]

def rejoin(txt):
    jn = ""
    for i in txt:
        if (i=="I"):
            jn += "j"
        elif (i!=" " and not i.isupper()):
            jn += i
    return jn