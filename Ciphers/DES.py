# DES Algorithm Implementation

import os

initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

perm_ch_1 = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]

perm_ch_2 = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

per = [16,  7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2,  8, 24, 14,
       32, 27,  3,  9,
       19, 13, 30,  6,
       22, 11,  4, 25]

def toBin(ch,rt=4):
    bi = ""
    temp = ord(ch)
    if (ord(ch)>=48 and ord(ch)<58 and rt==4):
        temp -= 48
    elif (ord(ch)>=97 and ord(ch)<103 and rt==4):
        temp -= 87
    while (temp>1):
        bi = str(temp%2) + bi
        temp //= 2
    if (temp==1):
        bi = "1" + bi
    while (len(bi)<rt):
        bi = "0" + bi
    return bi

def perm(st,num,inv=False):
    global initial_perm, perm_ch_1, perm_ch_2, per
    ls = []
    if (num==0):
        ls = initial_perm
    elif (num==1):
        ls = perm_ch_1
    elif (num==2):
        ls = perm_ch_2
    elif (num==3):
        ls = per
    b = []
    if (not inv):
        b = ls
    else:
        for i in range(len(ls)):
            b.append(ls.index(i+1)+1)
    c = ""
    for i in b:
        c += st[i-1]
    return c

def expand(txt):
    l = []
    temp = ""
    for i in txt:
        temp += i
        if (len(temp)==4):
            l.append(temp)
            temp = ""
    
    ret = ""
    m = []
    for i in range(len(l)):
        m.append(l[i-1][-1] + l[i] + l[(i+1)%8][0])
        ret += m[i]
    return ret

def sbox_reduce(txt):
    global sbox
    ret = ""
    temp = ""
    ctr = 0
    for i in txt:
        temp += i
        if (len(temp)==6):
            sr = (int(temp[0]) * 2) + (int(temp[5]) * 1)
            sc = (int(temp[1]) * 8) + (int(temp[2]) * 4) + (int(temp[3]) * 2) + (int(temp[4]) * 1)
            ch = sbox[ctr][sr][sc]
            ret += toBin(chr(ch))
            temp = ""
            ctr += 1
    return ret

def toTxt(txt,rt=4):
    ret = ""
    temp = 0
    ctr = rt - 1
    for i in txt:
        temp += int(i) * 2 ** ctr
        ctr -= 1
        if (ctr==-1):
            if (temp>=0 and temp<10 and rt==4):
                temp += 48
            elif (temp>=10 and temp<16 and rt==4):
                temp += 87
            ctr = rt - 1
            ret += chr(temp)
            temp = 0
    return ret


def encrypt(txt,ky):
    brk = []
    temp = ""
    for i in txt:
        temp += toBin(i)
        if (len(temp)==64):
            brk.append(temp)
            temp = ""
    if (temp!=""):
        while (len(temp)<64):
            temp += "0"
        brk.append(temp)
        temp = ""
    bcount = 1
    ct = ""
    for i in brk: 
        os.system('cls' if os.name == 'nt' else 'clear')   
        bl = perm(i,0)
        k = ""
        for x in ky:
            k += toBin(x)
        kp = perm(k,1)
        blk = i

        roundc = 1
        lc = bl[:32]
        rc = bl[32:]
        kc = kp

        while (roundc<17):
            print("Given Plaintext:",txt)
            print("Given Key:",ky)
            print("\n----------------------------------------------------Encryption Process----------------------------------------------------")
            print("\n\n\t\t\t\tInitial Setup (Block " + str(bcount) + ")-\n")
            print("Input Block:\t",toTxt(blk))
            print("Binary Block:\t",blk)
            print("Permuted Text:\t",bl)
            print("Key (64 Bit):\t",k)
            print("Key (56 Bit):\t",kp)
            print("\n\n\t\t\t\tRound " + str(roundc) + "-\n")
            print("L"+str(roundc)+":\t\t",lc)
            print("R"+str(roundc)+":\t\t",rc)

            klh = kc[:28]
            krh = kc[28:]
            if (roundc==1 or roundc==2 or roundc==9 or roundc==16):
                klh  = klh[1:] + klh[0]
                krh  = krh[1:] + krh[0]
            else:
                klh = klh[2:] + klh[:2]
                krh = krh[2:] + krh[:2]
            kc = klh + krh
            rk = perm(kc,2)
            print("Round Key:\t",rk)

            exp = expand(rc)
            print("Expanded R"+str(roundc)+":\t",exp)
            
            xor = ""
            for x in range(48):
                if (rk[x]==exp[x]):
                    xor += "0"
                else:
                    xor += "1"
            print("Xorred Output:\t",xor)

            red = sbox_reduce(xor)
            print("Sbox Reduction:\t",red)

            pmt = perm(red,3)
            print("Permuted Output:",pmt)

            rnext = ""
            for i in range(32):
                if (lc[i]==pmt[i]):
                    rnext += "0"
                else:
                    rnext += "1"
            print("Final Xor:\t",rnext)

            lc = rc
            rc = rnext
            roundc += 1

            if (roundc<17):
                print("\nL"+str(roundc)+":\t\t",toTxt(lc))
                print("R"+str(roundc)+":\t\t",toTxt(rc))
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("\nFinal L:\t",toTxt(lc))
                print("Final R:\t",toTxt(rc))
        print("Inverse IP:\t",toTxt(perm(rc + lc,0,True)))
        ct += perm(rc + lc,0,True)
        bcount += 1
    return toTxt(ct)

def decrypt(txt,ky):
    brk = []
    temp = ""
    for i in txt:
        temp += toBin(i)
        if (len(temp)==64):
            brk.append(temp)
            temp = ""
    if (temp!=""):
        while (len(temp)<64):
            temp += "0"
        brk.append(temp)
        temp = ""
    bcount = 1
    ct = ""
    for i in brk: 
        os.system('cls' if os.name == 'nt' else 'clear')   
        bl = perm(i,0)
        k = ""
        for x in ky:
            k += toBin(x)
        kp = perm(k,1)
        blk = i

        roundc = 16
        lc = bl[:32]
        rc = bl[32:]
        kc = kp

        while (roundc>=1):
            print("Received Ciphertext:",txt)
            print("Given Key:",ky)
            print("\n----------------------------------------------------Decryption Process----------------------------------------------------")
            print("\n\n\t\t\t\tInitial Setup (Block " + str(bcount) + ")-\n")
            print("Input Block:\t",toTxt(blk))
            print("Binary Block:\t",blk)
            print("Permuted Text:\t",bl)
            print("Key (64 Bit):\t",k)
            print("Key (56 Bit):\t",kp)
            print("\n\n\t\t\t\tRound " + str(17-roundc) + "-\n")
            print("L"+str(roundc)+":\t\t",lc)
            print("R"+str(roundc)+":\t\t",rc)

            klh = kp[:28]
            krh = kp[28:]
            temp_rc = 1
            while (temp_rc!=roundc+1):
                if (temp_rc==1 or temp_rc==2 or temp_rc==9 or temp_rc==16):
                    klh  = klh[1:] + klh[0]
                    krh  = krh[1:] + krh[0]
                else:
                    klh = klh[2:] + klh[:2]
                    krh = krh[2:] + krh[:2]
                kc = klh + krh
                temp_rc += 1
            rk = perm(kc,2)
            print("Round Key:\t",rk)

            exp = expand(rc)
            print("Expanded R"+str(roundc)+":\t",exp)
            
            xor = ""
            for x in range(48):
                if (rk[x]==exp[x]):
                    xor += "0"
                else:
                    xor += "1"
            print("Xorred Output:\t",xor)

            red = sbox_reduce(xor)
            print("Sbox Reduction:\t",red)

            pmt = perm(red,3)
            print("Permuted Output:",pmt)

            rnext = ""
            for i in range(32):
                if (lc[i]==pmt[i]):
                    rnext += "0"
                else:
                    rnext += "1"
            print("Final Xor:\t",rnext)

            lc = rc
            rc = rnext
            roundc -= 1

            if (roundc>=1):
                print("\nL"+str(roundc)+":\t\t",toTxt(lc))
                print("R"+str(roundc)+":\t\t",toTxt(rc))
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("\nFinal L:\t",toTxt(lc))
                print("Final R:\t",toTxt(rc))
        print("Inverse IP:\t",toTxt(perm(rc + lc,0,True)))
        ct += perm(rc + lc,0,True)
        bcount += 1
    return toTxt(ct)