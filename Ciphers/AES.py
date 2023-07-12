# AES Algorithm Implementation

import os
from tabulate import tabulate

sbox = [["63","7c","77","7b","f2","6b","6f","c5","30","01","67","2b","fe","d7","ab","76"],
        ["ca","82","c9","7d","fa","59","47","f0","ad","d4","a2","af","9c","a4","72","c0"],
        ["b7","fd","93","26","36","3f","f7","cc","34","a5","e5","f1","71","d8","31","15"],
        ["04","c7","23","c3","18","96","05","9a","07","12","80","e2","eb","27","b2","75"],
        ["09","83","2c","1a","1b","6e","5a","a0","52","3b","d6","b3","29","e3","2f","84"],
        ["53","d1","00","ed","20","fc","b1","5b","6a","cb","be","39","4a","4c","58","cf"],
        ["d0","ef","aa","fb","43","4d","33","85","45","f9","02","7f","50","3c","9f","a8"],
        ["51","a3","40","8f","92","9d","38","f5","bc","b6","da","21","10","ff","f3","d2"],
        ["cd","0c","13","ec","5f","97","44","17","c4","a7","7e","3d","64","5d","19","73"],
        ["60","81","4f","dc","22","2a","90","88","46","ee","b8","14","de","5e","0b","db"],
        ["e0","32","3a","0a","49","06","24","5c","c2","d3","ac","62","91","95","e4","79"],
        ["e7","c8","37","6d","8d","d5","4e","a9","6c","56","f4","ea","65","7a","ae","08"],
        ["ba","78","25","2e","1c","a6","b4","c6","e8","dd","74","1f","4b","bd","8b","8a"],
        ["70","3e","b5","66","48","03","f6","0e","61","35","57","b9","86","c1","1d","9e"],
        ["e1","f8","98","11","69","d9","8e","94","9b","1e","87","e9","ce","55","28","df"],
        ["8c","a1","89","0d","bf","e6","42","68","41","99","2d","0f","b0","54","bb","16"]]

mix = [[2,3,1,1],
       [1,2,3,1],
       [1,1,2,3],
       [3,1,1,2]]

inv_mix = [["e","b","d","9"],
           ["9","e","b","d"],
           ["d","9","e","b"],
           ["b","d","9","e"]]

rcon = [["01","02","04","08","10","20","40","80","1b","36"],
        ["00","00","00","00","00","00","00","00","00","00"],
        ["00","00","00","00","00","00","00","00","00","00"],
        ["00","00","00","00","00","00","00","00","00","00"]]

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

def inv_column(mat):
    global inv_mix
    ret = [["","","",""],
           ["","","",""],
           ["","","",""],
           ["","","",""]]
    for i in range(4):
        ls = [mat[0][i],mat[1][i],mat[2][i],mat[3][i]]
        cnt = 0
        for j in inv_mix:
            res = "00000000"
            for k in range(4):
                inv = toBin(j[k])
                inter = "00000000"
                for x in range(3):
                    mul = toBin(ls[k][0]) + toBin(ls[k][1])
                    if (inv[x]=="1"):
                        ex = 3 - x
                        mul += "0" * ex
                        rp = mul[:ex]
                        mul = mul[ex:]
                        for y in range(ex):
                            if (rp[y]=="1"):
                                pw = 7 + ex - y
                                xor = "00011011"
                                while (pw != 8):
                                    xor = xor[1:] + xor[0]
                                    pw -= 1
                                temp = mul
                                mul = ""
                                for z in range(len(temp)):
                                    mul += str((int(xor[z]) + int(temp[z])) % 2)
                        temp = inter
                        inter = ""
                        for z in range(len(temp)):
                            inter += str((int(mul[z]) + int(temp[z])) % 2)
                if (inv[-1]=="1"):
                    mul = toBin(ls[k][0]) + toBin(ls[k][1])
                    temp = inter
                    inter = ""
                    for z in range(len(temp)):
                        inter += str((int(mul[z]) + int(temp[z])) % 2)
                temp = res
                res = ""
                for z in range(len(temp)):
                    res += str((int(inter[z]) + int(temp[z])) % 2)
            ret[cnt][i] = toTxt(res)
            cnt += 1
    return ret

def tbprint(ip,sb,sh,mx,rk):
    tip = tabulate(ip,tablefmt="fancy_grid").split("\n")
    tsb = tabulate(sb,tablefmt="fancy_grid").split("\n")
    tsh = tabulate(sh,tablefmt="fancy_grid").split("\n")
    tmx = tabulate(mx,tablefmt="fancy_grid").split("\n")
    tky = tabulate(rk,tablefmt="fancy_grid").split("\n")

    for i in range(len(tip)):
        print(tip[i]+"\t"+tsb[i]+"\t"+tsh[i]+"\t"+tmx[i]+"\t"+tky[i])

def encrypt(txt,ky,aes=1):
    global sbox,mix,rcon
    rounds = 0
    bits = 0
    if (aes==1):
        rounds = 10
        bits = 128
    val = bits // 8
    if (len(txt)%val!=0):
        txt += " " * (val - (len(txt) % val))
    bi = ""
    kybin = ""
    for i in txt:
        bi += toBin(i)
    for i in ky:
        kybin += toBin(i)
    states = []
    st = []
    temp = []
    hx = ""
    ps = ""
    for i in bi:
        hx += i
        if (len(hx)==4):
            ps += toTxt(hx)
            if (len(ps)==2):
                temp.append(ps)
                if (len(temp)==4):
                    st.append(temp)
                    if (len(st)==4):
                        states.append(st)
                        st = []
                    temp = []
                ps = ""
            hx = ""

    for i in kybin:
        hx += i
        if (len(hx)==4):
            ps += toTxt(hx)
            if (len(ps)==2):
                temp.append(ps)
                if (len(temp)==4):
                    st.append(temp)
                    temp = []
                ps = ""
            hx = ""
    
    ret = ""
    for sti in range(len(states)):
        rip = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        rsb = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        rsh = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        rmx = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        rky = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        for i in range(len(states[sti])):
            for j in range(len(states[sti][i])):
                rip[i][j] = states[sti][i][j]
        for i in range(len(st)):
            for j in range(len(st[i])):
                rky[i][j] = st[i][j]

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Given Plaintext:",txt)
        print("Given Key:",ky)
        print("_________________________________________________________________________________________________________________________")
        print("Current Block:",end=" ")
        blk = ""
        for i in states[sti]:
            for j in i:
                blk += j
        print(blk)
        print("\n     Round Input","  After Substitution","   After Row Shift"," After Column Mixing","      Round Key",sep="\t")
        print("")
        tbprint(rip,rsb,rsh,rmx,rky)
        for i in range(len(rip)):
            for j in range(len(rip[i])):
                rmx[i][j] = rip[i][j]

        rnd = 1
        while (rnd<=rounds):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Given Plaintext:",txt)
            print("Given Key:",ky)
            print("_________________________________________________________________________________________________________________________")
            print("Current Block:",end=" ")
            blk = ""
            for i in states[sti]:
                for j in i:
                    blk += j
            print(blk)
            print("\n     Round Input","  After Substitution","   After Row Shift"," After Column Mixing","      Round Key",sep="\t")
            print("")
            if (rnd!=1):
                tbprint(rip,rsb,rsh,rmx,rky)
            else:
                tbprint(rip,rsb,rsh,rsh,rky)
            for i in range(len(rmx)):
                for j in range(len(rmx[i])):
                    num1 = toBin(rmx[i][j][0])+toBin(rmx[i][j][1])
                    num2 = toBin(rky[i][j][0])+toBin(rky[i][j][1])
                    ps = ""
                    for x in range(len(num1)):
                        if (num1[x]==num2[x]):
                            ps += "0"
                        else:
                            ps += "1"
                    rip[i][j] = toTxt(ps)

            for i in range(len(rip)):
                for j in range(len(rip[i])):
                    r = toBin(rip[i][j][0])
                    c = toBin(rip[i][j][1])
                    for x in range(16):
                        if (toBin(chr(x))==r):
                            for y in range(16):
                                if (toBin(chr(y))==c):
                                    rsb[i][j] = sbox[x][y]

            for i in range(len(rsb)):
                for j in range(len(rsb[i])):
                    rsh[i][j] = rsb[i][j]
            for i in range(1,len(rsb)):
                for j in range(i):
                    dum = rsh[i][0]
                    for k in range(3):
                        rsh[i][k] = rsh[i][k+1]
                    rsh[i][k+1] = dum
            
            if (rnd!=rounds):
                for i in range(4):
                    ls = [rsh[0][i],rsh[1][i],rsh[2][i],rsh[3][i]]
                    ind = 0
                    for j in mix:
                        hexnum = "00000000"
                        for k in range(len(j)):
                            num = toBin(ls[k][0]) + toBin(ls[k][1])
                            if (j[k]==1):
                                for x in range(len(hexnum)):
                                    if (hexnum[x]==num[x]):
                                        hexnum = hexnum[:x] + "0" + hexnum[x+1:]
                                    else:
                                        hexnum = hexnum[:x] + "1" + hexnum[x+1:]
                            elif (j[k]==2):
                                newnum = num + "0"
                                finnum = ""
                                if (newnum[0]=="1"):
                                    newnum = newnum[1:]
                                    poly = "00011011"
                                    for x in range(len(poly)):
                                        if (newnum[x]==poly[x]):
                                            finnum += "0"
                                        else:
                                            finnum += "1"
                                else:
                                    finnum = newnum[1:]
                                for x in range(len(hexnum)):
                                    if (hexnum[x]==finnum[x]):
                                        hexnum = hexnum[:x] + "0" + hexnum[x+1:]
                                    else:
                                        hexnum = hexnum[:x] + "1" + hexnum[x+1:]
                            elif (j[k]==3):
                                newnum = num + "0"
                                finnum = ""
                                tempnum = ""
                                if (newnum[0]=="1"):
                                    newnum = newnum[1:]
                                    poly = "00011011"
                                    for x in range(len(poly)):
                                        if (newnum[x]==poly[x]):
                                            tempnum += "0"
                                        else:
                                            tempnum += "1"
                                else:
                                    tempnum = newnum[1:]
                                for x in range(len(num)):
                                    if (num[x]==tempnum[x]):
                                        finnum += "0"
                                    else:
                                        finnum += "1"
                                for x in range(len(hexnum)):
                                    if (hexnum[x]==finnum[x]):
                                        hexnum = hexnum[:x] + "0" + hexnum[x+1:]
                                    else:
                                        hexnum = hexnum[:x] + "1" + hexnum[x+1:]
                        rmx[ind][i] = toTxt(hexnum)
                        ind += 1
            else:
                rmx = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
            
            tempmat = []
            for i in range(len(rky)):
                newls = []
                for j in range(len(rky[i])):
                    newls.append(rky[i][j])
                tempmat.append(newls)
            chg = True
            for i in range(len(tempmat)):
                for j in range(len(tempmat)):
                    hx1 = ""
                    hx2 = ""
                    if (chg):
                        r = toBin(tempmat[((j + 1) % 4)][3][0])
                        c = toBin(tempmat[((j + 1) % 4)][3][1])
                        for x in range(16):
                            if (toBin(chr(x))==r):
                                for y in range(16):
                                    if (toBin(chr(y))==c):
                                        hx1 = sbox[x][y]
                        hx2 = rcon[j][rnd-1]
                    else:
                        hx1 = rky[j][i-1]
                        hx2 = tempmat[j][i]
                    bi1 = toBin(hx1[0]) + toBin(hx1[1])
                    bi2 = toBin(hx2[0]) + toBin(hx2[1])
                    finbi = ""
                    for x in range(len(bi1)):
                        if (bi1[x]==bi2[x]):
                            finbi += "0"
                        else:
                            finbi += "1"
                    if (chg):
                        hx3 = tempmat[j][0]
                        bi3 = toBin(hx3[0]) + toBin(hx3[1])
                        tempbi = ""
                        for x in range(len(finbi)):
                            if (finbi[x]==bi3[x]):
                                tempbi += "0"
                            else:
                                tempbi += "1"
                        finbi = tempbi
                    rky[j][i] = toTxt(finbi)
                chg = False

            tbprint(rip,rsb,rsh,rmx,rky)
            rnd += 1
        cp = [["","","",""],
              ["","","",""],
              ["","","",""],
              ["","","",""]]
        for i in range(len(rsh)):
            for j in range(len(rsh[i])):
                num1 = toBin(rsh[i][j][0])+toBin(rsh[i][j][1])
                num2 = toBin(rky[i][j][0])+toBin(rky[i][j][1])
                ps = ""
                for x in range(len(num1)):
                    if (num1[x]==num2[x]):
                        ps += "0"
                    else:
                        ps += "1"
                cp[i][j] = toTxt(ps)
        print(tabulate(cp,tablefmt="fancy_grid"))
        print("\nCiphertext for the block:",end=" ")
        ct = ""
        for i in cp:
            for j in i:
                ct += j
        print(ct)
        ret += ct
    return ret

def decrypt(txt,ky,aes=1):
    global sbox,mix,rcon
    rounds = 0
    bits = 0
    if (aes==1):
        rounds = 10
        bits = 128
    val = bits // 8
    if (len(txt)%val!=0):
        txt += " " * (val - (len(txt) % val))
    bi = ""
    kybin = ""
    for i in txt:
        bi += toBin(i)
    for i in ky:
        kybin += toBin(i)
    states = []
    st = []
    temp = []
    hx = ""
    ps = ""
    for i in bi:
        hx += i
        if (len(hx)==4):
            ps += toTxt(hx)
            if (len(ps)==2):
                temp.append(ps)
                if (len(temp)==4):
                    st.append(temp)
                    if (len(st)==4):
                        states.append(st)
                        st = []
                    temp = []
                ps = ""
            hx = ""

    for i in kybin:
        hx += i
        if (len(hx)==4):
            ps += toTxt(hx)
            if (len(ps)==2):
                temp.append(ps)
                if (len(temp)==4):
                    st.append(temp)
                    temp = []
                ps = ""
            hx = ""
    
    ret = ""
    for sti in range(len(states)):
        rip = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        rak = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        rsh = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        rmx = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        rky = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
        for i in range(len(states[sti])):
            for j in range(len(states[sti][i])):
                rip[i][j] = states[sti][i][j]

        rnd = 0
        while (rnd<=rounds):
            for i in range(len(st)):
                for j in range(len(st[i])):
                    rky[i][j] = st[i][j]
            
            for keycnt in range(rounds-rnd):
                tempmat = []
                for i in range(len(rky)):
                    newls = []
                    for j in range(len(rky[i])):
                        newls.append(rky[i][j])
                    tempmat.append(newls)
                chg = True
                for i in range(len(tempmat)):
                    for j in range(len(tempmat)):
                        hx1 = ""
                        hx2 = ""
                        if (chg):
                            r = toBin(tempmat[((j + 1) % 4)][3][0])
                            c = toBin(tempmat[((j + 1) % 4)][3][1])
                            for x in range(16):
                                if (toBin(chr(x))==r):
                                    for y in range(16):
                                        if (toBin(chr(y))==c):
                                            hx1 = sbox[x][y]
                            hx2 = rcon[j][keycnt]
                        else:
                            hx1 = rky[j][i-1]
                            hx2 = tempmat[j][i]
                        bi1 = toBin(hx1[0]) + toBin(hx1[1])
                        bi2 = toBin(hx2[0]) + toBin(hx2[1])
                        finbi = ""
                        for x in range(len(bi1)):
                            if (bi1[x]==bi2[x]):
                                finbi += "0"
                            else:
                                finbi += "1"
                        if (chg):
                            hx3 = tempmat[j][0]
                            bi3 = toBin(hx3[0]) + toBin(hx3[1])
                            tempbi = ""
                            for x in range(len(finbi)):
                                if (finbi[x]==bi3[x]):
                                    tempbi += "0"
                                else:
                                    tempbi += "1"
                            finbi = tempbi
                        rky[j][i] = toTxt(finbi)
                    chg = False

            for i in range(len(rip)):
                for j in range(len(rip[i])):
                    num1 = toBin(rip[i][j][0])+toBin(rip[i][j][1])
                    num2 = toBin(rky[i][j][0])+toBin(rky[i][j][1])
                    ps = ""
                    for x in range(len(num1)):
                        if (num1[x]==num2[x]):
                            ps += "0"
                        else:
                            ps += "1"
                    rak[i][j] = toTxt(ps)
            
            if (rnd!=0 and rnd!=rounds):
                mat = inv_column(rak)
                for x in range(len(mat)):
                    for y in range(len(mat[x])):
                        rmx[x][y] = mat[x][y]
            else:
                rmx = [["--","--","--","--"],["--","--","--","--"],["--","--","--","--"],["--","--","--","--"]]
            
            if (rnd==0):
                for i in range(len(rak)):
                    for j in range(len(rak[i])):
                        rsh[i][j] = rak[i][j]
            else:
                for i in range(len(rmx)):
                    for j in range(len(rmx[i])):
                        rsh[i][j] = rmx[i][j]
            for i in range(1,len(rsh)):
                for j in range(i):
                    dum = rsh[i][-1]
                    for k in range(3,0,-1):
                        rsh[i][k] = rsh[i][k-1]
                    rsh[i][0] = dum
    
            if (rnd!=0):
                tbprint(rip,rky,rak,rmx,rsh)
            if (rnd!=rounds):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Given Plaintext:",txt)
                print("Given Key:",ky)
                print("_________________________________________________________________________________________________________________________")
                print("Current Block:",end=" ")
                blk = ""
                for i in states[sti]:
                    for j in i:
                        blk += j
                print(blk)
                print("\n     Round Input","      Round Key ","   After Round Key"," After Column Mixing","   After Row Shift",sep="\t")
                print("")
                tbprint(rip,rky,rak,rmx,rsh)
            if (rnd==0):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Given Plaintext:",txt)
                print("Given Key:",ky)
                print("_________________________________________________________________________________________________________________________")
                print("Current Block:",end=" ")
                blk = ""
                for i in states[sti]:
                    for j in i:
                        blk += j
                print(blk)
                print("\n     Round Input","      Round Key ","   After Round Key"," After Column Mixing","   After Row Shift",sep="\t")
                print("")
                tbprint(rip,rky,rak,rmx,rsh)

            for i in range(len(rsh)):
                for j in range(len(rsh[i])):
                    for x in range(len(sbox)):
                        for y in range(len(sbox[x])):
                            if (sbox[x][y]==rsh[i][j]):
                                rip[i][j] = toTxt(toBin(chr(x))+toBin(chr(y)))

            rnd += 1
        cp = [["","","",""],
              ["","","",""],
              ["","","",""],
              ["","","",""]]
        for i in range(len(rsh)):
            for j in range(len(rsh[i])):
                cp[i][j] = rak[i][j]
        print(tabulate(cp,tablefmt="fancy_grid"))
        print("\nPlaintext for the block:",end=" ")
        ct = ""
        for i in cp:
            for j in i:
                ct += j
        print(ct)
        ret += ct
    return ret