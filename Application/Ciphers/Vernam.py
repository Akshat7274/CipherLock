# Vernam Cipher Implementation

def keymap(txt,key):
    k = 0
    ret = ""
    for i in txt:
        if (i==" "):
            ret += " "
        else:
            ret += key[k%len(key)]
        k += 1
    return ret

def binary(txt):
    ret = ""
    for i in txt:
        temp = ""
        asc = ord(i) - 97
        while (asc!=0):
            temp = str(asc%2) + temp
            asc //= 2
        while (len(temp)<5):
            temp = "0" + temp
        ret += temp + " "
    return ret[0:-1]

def xoring(bs1,bs2):
    ret = ""
    for i in range(len(bs1)):
        if (bs1[i]==" "):
            ret += " "
        elif (bs1[i]==bs2[i]):
            ret += "0"
        else:
            ret += "1"
    return ret

def txtcvt(bs):
    buff = bs.split(" ")
    ret = ""
    for i in buff:
        sm = 0
        pw = 0
        while (len(i)>0):
            sm += (2**pw)*int(i[-1])
            pw += 1
            i = i[0:-1]
        ret += chr((sm)+97)
    return ret