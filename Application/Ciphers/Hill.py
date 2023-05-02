# Hill Cipher Implementation

import math
from tabulate import tabulate

def key_generate(ky,sz):
    mat = []
    mul = []
    temp = []
    temp_mul = []
    for i in ky:
        temp.append(i)
        temp_mul.append(ord(i)-97)
        if (len(temp)==sz):
            mat.append(temp)
            mul.append(temp_mul)
            temp = []
            temp_mul = []
    return mat,mul

def codeword(txt,sz):
    fin = []
    spl = []
    if (int(len(txt)%sz)!=0):
        txt += "X"*(int(sz)-int(len(txt)%sz))
    for i in txt:
        spl.append([i])
        if (len(spl)==sz):
            fin.append(spl)
            spl = []
    return fin

def cvt(cdw):
    tmp = []
    temp = []
    for i in cdw:
        for j in i:
            for k in j:
                if (k.islower()):
                    temp.append([ord(k)-97])
                elif (k=="A"):
                    temp.append(["0"])
                else:
                    temp.append([(ord(k)-65)*-1])
        tmp.append(temp)
        temp = []
    return tmp

def calc_mat(ky,tx,sz):
    ret = [tabulate(ky,tablefmt="fancy_grid"),
           tabulate(tx,tablefmt="fancy_grid"),
           "\n"*int((math.sqrt(sz)/2)*2) + "="]
    res = []
    res26 = []
    fin = []
    k = 0
    txt = ""
    count = 0
    for i in ky:
        sum = 0
        for j in i:
            check = False
            neg = False
            if (tx[k][0]=="0"):
                tx[k][0] = 0
                check = True
                if (count==k):
                    neg = True
            if (sum<0):
                sum *= -1
                if(tx[k][0]<0):
                    tx[k][0] *= -1
                    sum += j*tx[k][0]
                    tx[k][0] *= -1
                else:
                    sum += j*tx[k][0]
                sum *= -1
            else:
                if(tx[k][0]<0):
                    tx[k][0] *= -1
                    sum += j*tx[k][0]
                    tx[k][0] *= -1
                else:
                    sum += j*tx[k][0]
            if  (tx[k][0]<0 and count==k):
                sum *= -1
            elif (neg):
                sum *= -1
            if (check):
                tx[k][0] = "0"
            k += 1
        k = 0
        count += 1
        res.append([sum])
        if(sum<0):
            sum *= -1
            res26.append([(sum%26)*-1])
            fin.append([chr((sum%26)+65)])
            txt += chr((sum%26)+65)
        else:
            res26.append([(sum%26)])
            fin.append([chr((sum%26)+97)])
            txt += chr((sum%26)+97)
    ret.append(tabulate(res,tablefmt="fancy_grid"))
    ret.append("\n"*int((math.sqrt(sz)/2)*2) + "(mod 26) =")
    ret.append(tabulate(res26,tablefmt="fancy_grid"))
    ret.append("\n"*int((math.sqrt(sz)/2)*2) + "=")
    ret.append(tabulate(fin,tablefmt="fancy_grid"))
    fin_ret = []
    fin_ret.append(ret)
    return fin_ret,txt

def modulo(num,mod=26):
    m = mod
    y = 0
    x = 1

    while (num>1):
        q = num//mod
        t = mod
        mod  = num%mod
        num = t
        t = y

        y = x - q * y
        x = t
    if (x<0):
        x += m

    return x


def det(m):
    if (len(m)==2):
        return (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
    else:
        mat = []
        temp = []
        deter = 0
        for i in range(len(m)):
            pw = (-1)**(0+i)
            for j in range(len(m)):
                if (j!=0):
                    for k in range(len(m)):
                        if (k!=i):
                            temp.append(m[j][k])
                    mat.append(temp)
                    temp = []
            deter += pw*det(mat)*m[0][i]
            mat = []
        return deter

def inv(m):
    deter = det(m)%26
    mod = modulo(deter)
    adj = []
    for temp in range(len(m)):
        adj.append([0*t for t in range(len(m))])
    for i in range(len(m)):
        for j in range(len(m)):
            mn = []
            tp = []
            pw = (-1)**(i+j)
            for x in range(len(m)):
                if (x!=i):
                    for y in range(len(m)):
                        if (y!=j):
                            tp.append(m[x][y])
                    mn.append(tp)
                    tp = []
            adj[j][i] = (pw*det(mn)*mod)%26
    
    return adj
    

def encrpyt(inp,key,n):
    print("\n\n----------------------------------------------------Encryption Process----------------------------------------------------\n")
    key_mat,key_mul = key_generate(key.lower(),math.sqrt(n))
    key_p = [[tabulate(key_mat,tablefmt="fancy_grid"),"\n"*int((math.sqrt(n)/2)*2) + "=",tabulate(key_mul,tablefmt="fancy_grid")]]
    cw_p = [[tabulate(i,tablefmt="fancy_grid") for i in codeword(inp.lower(),math.sqrt(n))]]
    cw_p[0].append("\n"*int((math.sqrt(n)/2)*2) + "=")
    temp1 = [tabulate(i,tablefmt="fancy_grid") for i in cvt(codeword(inp.lower(),math.sqrt(n)))]
    for i in temp1:
        cw_p[0].append(i)
    set_print = [["Key Matrix","Code Word Bifurcation"],[tabulate(key_p,headers="firstrow"),tabulate(cw_p,headers="firstrow")]]
    print(tabulate(set_print,tablefmt="fancy_grid"))
    ct = ""
    for i in cvt(codeword(inp.lower(),math.sqrt(n))):
        pr,cd = calc_mat(key_mul,i,n)
        print(tabulate(pr,headers="firstrow"))
        ct += cd

    print("\nFinal Ciphertext:",ct)
    return ct

def decrypt(ct,key,n):
    print("\n\n----------------------------------------------------Decryption Process----------------------------------------------------\n")
    key_mat,key_mul = key_generate(key.lower(),math.sqrt(n))
    key_p = [[tabulate(key_mat,tablefmt="fancy_grid"),"-1","\n"*int((math.sqrt(n)/2)*2) + "=",tabulate(key_mul,tablefmt="fancy_grid"),"-1","\n"*int((math.sqrt(n)/2)*2) + "=",tabulate(inv(key_mul),tablefmt="fancy_grid")]]
    cw_p = [[tabulate(i,tablefmt="fancy_grid") for i in codeword(ct,math.sqrt(n))]]
    cw_p[0].append("\n"*int((math.sqrt(n)/2)*2) + "=")
    temp1 = [tabulate(i,tablefmt="fancy_grid") for i in cvt(codeword(ct,math.sqrt(n)))]
    for i in temp1:
        cw_p[0].append(i)
    set_print = [["Key Matrix Inverse","Code Word Bifurcation"],[tabulate(key_p,headers="firstrow"),tabulate(cw_p,headers="firstrow")]]
    print(tabulate(set_print,tablefmt="fancy_grid"))
    pt = ""
    for i in cvt(codeword(ct,math.sqrt(n))):
        pr,cd = calc_mat(inv(key_mul),i,n)
        print(tabulate(pr,headers="firstrow"))
        pt += cd

    print("\nDeciphered text:",pt)
    return pt