import random
from django.shortcuts import render
from Ciphers import Caesar, Playfair, Hill, Vigenere, Vernam, Railfence, RailfenceNew, RCTransform, DES, AES, RSA, DiffieHellman, ElGamal
from .forms import CaesarForm, PlayfairForm, HillForm, VigenereForm, VernamForm, RailfenceForm, RCTForm, DESForm, AESForm, RSAForm, DFForm, ElGamalForm
import math
import hashlib

# Create your views here.

def index(request):
    return render(request,'index.html')

def caesar(request):
    if request.method == "POST":
        form = CaesarForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                dec = Caesar.decrypt(request.POST['ct'],int(request.POST['key'])).split("\r\n")
                form = CaesarForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                enc = Caesar.encrypt(request.POST['pt'],int(request.POST['key'])).split("\r\n")
                form = CaesarForm(request.POST)
            return render(request, "caesar.html", {"form":form, "error":error, "extra":extra, "enc":enc, "dec":dec})
    else:
        form = CaesarForm()
    return render(request,"caesar.html",{"form":form})

def playfair(request):
    if request.method == "POST":
        form = PlayfairForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                lsplit = request.POST['ct'].split("\r\n")
                for txt in lsplit:
                    spText = txt.split(" ")
                    temp = ""
                    for i in spText:
                        temp += Playfair.rejoin(Playfair.decrypt(i,Playfair.key_matrix(request.POST['key']))) + " "
                    temp = temp[0:-1]
                    dec.append(temp)
                form = PlayfairForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                lsplit = request.POST['pt'].split("\r\n")
                for txt in lsplit:
                    spText = txt.split(" ")
                    temp = ""
                    for i in spText:
                        temp += Playfair.encrypt(Playfair.txtsplit(i),Playfair.key_matrix(request.POST['key'])) + " "
                    temp = temp[0:-1]
                    enc.append(temp)
                form = PlayfairForm(request.POST)
            return render(request, "playfair.html", {"form":form, "error":error, "extra":extra, "enc":enc, "dec":dec})
    else:
        form = PlayfairForm()
    return render(request,"playfair.html",{"form":form})

def hill(request):
    if request.method == "POST":
        form = HillForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            l = len(request.POST['key'])
            if (math.sqrt(l)!=int(math.sqrt(l))):
                error = "The entered key is not valid! Kindly enter an NxN key"
            elif (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                lsplit = request.POST['ct'].split("\r\n")
                for txt in lsplit:
                    temp = ""
                    for i in txt.split(" "):
                        response = Hill.decrypt(i,request.POST['key'],l)
                        for x in response:
                            if (x.islower()):
                                temp += x
                        temp += " "
                    temp = temp[0:-1]
                    dec.append(temp)
                form = HillForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                lsplit = request.POST['pt'].split("\r\n")
                for txt in lsplit:
                    temp = ""
                    for i in txt.split(" "):
                        temp += Hill.encrpyt(i,request.POST['key'],l) + " "
                    temp = temp[0:-1]
                    enc.append(temp)
                form = HillForm(request.POST)
            return render(request, "hill.html", {"form":form, "error":error, "extra":extra, "enc":enc,"dec":dec})
    else:
        form = HillForm()
    return render(request,"hill.html",{"form":form})

def vigenere(request):
    if request.method == "POST":
        form = VigenereForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                lsplit = request.POST['ct'].split("\r\n")
                for txt in lsplit:
                    dec.append(Vigenere.decrypt(txt,request.POST['key'])[-1][-1])
                form = VigenereForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                lsplit = request.POST['pt'].split("\r\n")
                for txt in lsplit:
                    enc.append(Vigenere.encrypt(txt,request.POST['key'])[-1][-1])
                form = VigenereForm(request.POST)
            return render(request, "vigenere.html", {"form":form, "error":error, "extra":extra, "enc":enc, "dec":dec})
    else:
        form = VigenereForm()
    return render(request,"vigenere.html",{"form":form})

def vernam(request):
    if request.method == "POST":
        form = VernamForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                lsplit = request.POST['ct'].split("\r\n")
                for txt in lsplit:
                    temp = ""
                    for i in txt.split(" "):
                        temp += Vernam.txtcvt(Vernam.xoring(Vernam.binary(i),Vernam.binary(request.POST['key']))) + " "
                    temp = temp[0:-1]
                    dec.append(temp)
                form = VernamForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                lsplit = request.POST['pt'].split("\r\n")
                for txt in lsplit:
                    temp = ""
                    for i in txt.split(" "):
                        temp += Vernam.txtcvt(Vernam.xoring(Vernam.binary(i),Vernam.binary(request.POST['key']))) + " "
                    temp = temp[0:-1]
                    enc.append(temp)
                form = VernamForm(request.POST)
            return render(request, "vernam.html", {"form":form, "error":error, "extra":extra, "enc":enc, "dec":dec})
    else:
        form = VernamForm()
    return render(request,"vernam.html",{"form":form})

def railfence(request):
    if request.method == "POST":
        form = RailfenceForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                lsplit = request.POST['ct'].split("\r\n")
                for txt in lsplit:
                    dec.append(Railfence.decrypt(txt,int(request.POST['key'])))
                form = RailfenceForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                lsplit = request.POST['pt'].split("\r\n")
                for txt in lsplit:
                    enc.append(Railfence.encrypt(txt,int(request.POST['key'])))
                form = RailfenceForm(request.POST)
            return render(request, "railfence-conv.html", {"form":form, "error":error, "extra":extra, "enc":enc, "dec":dec})
    else:
        form = RailfenceForm()
    return render(request,"railfence-conv.html",{"form":form})

def railfenceNew(request):
    if request.method == "POST":
        form = RailfenceForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                lsplit = request.POST['ct'].split("\r\n")
                for txt in lsplit:
                    dec.append(RailfenceNew.decrypt(txt,int(request.POST['key'])))
                form = RailfenceForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                lsplit = request.POST['pt'].split("\r\n")
                for txt in lsplit:
                    enc.append(RailfenceNew.encrypt(txt,int(request.POST['key'])))
                form = RailfenceForm(request.POST)
            return render(request, "railfence-new.html", {"form":form, "error":error, "extra":extra, "enc":enc, "dec":dec})
    else:
        form = RailfenceForm()
    return render(request,"railfence-new.html",{"form":form})

def rcTransform(request):
    if request.method == "POST":
        form = RCTForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                lsplit = request.POST['ct'].split("\r\n")
                for txt in lsplit:
                    dec.append(RCTransform.decrypt(txt,request.POST['key']))
                form = RCTForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                lsplit = request.POST['pt'].split("\r\n")
                for txt in lsplit:
                    enc.append(RCTransform.encrypt(txt,request.POST['key']))
                form = RCTForm(request.POST)
            return render(request, "rc-transform.html", {"form":form, "error":error, "extra":extra, "enc":enc, "dec":dec})
    else:
        form = RCTForm()
    return render(request,"rc-transform.html",{"form":form})

def des(request):
    if request.method == "POST":
        form = DESForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (len(request.POST['key'])!=8):
                error = "The key has to be 8 characters long"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                lsplit = request.POST['ct'].split("\r\n")
                for txt in lsplit:
                    inp = txt
                    key = request.POST['key']
                    hexinp = ""
                    for i in inp:
                        hexinp += DES.toTxt(DES.toBin(i,8))
                    hexkey = ""
                    for i in key:
                        hexkey += DES.toTxt(DES.toBin(i,8))
                    dec_out = DES.decrypt(hexinp,hexkey)
                    txt = ""
                    for i in dec_out:
                        txt += DES.toBin(i)
                    fin = DES.toTxt(txt,8)
                    it = -1
                    while (fin[it]==" "):
                        it -= 1
                    if (it==-1):
                        it = len(fin) - 1
                    fin = fin[:it+1]
                    dec.append(fin)
                form = DESForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                lsplit = request.POST['pt'].split("\r\n")
                for txt in lsplit:
                    inp = txt
                    key = request.POST['key']
                    if (len(inp)%8!=0):
                        inp += " " * (8 - (len(inp) % 8))
                    hexinp = ""
                    for i in inp:
                        hexinp += DES.toTxt(DES.toBin(i,8))
                    hexkey = ""
                    for i in key:
                        hexkey += DES.toTxt(DES.toBin(i,8))
                    enc_out = DES.encrypt(hexinp,hexkey)
                    txt = ""
                    for i in enc_out:
                        txt += DES.toBin(i)
                    enc.append(DES.toTxt(txt,8))
                form = DESForm(request.POST)
            return render(request, "des.html", {"form":form, "error":error, "extra":extra, "enc":enc, "dec":dec})
    else:
        form = DESForm()
    return render(request,"des.html",{"form":form})

def aes(request):
    if request.method == "POST":
        form = AESForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            enc = []
            dec = []
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")!="" and request.POST.get("ct")!=""):
                error = "Both operations can not be done together. Kindly clear one of the inputs!"
            elif (len(request.POST['key'])!=16):
                error = "The key has to be 16 characters long. Only AES-128 supported!"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                lsplit = request.POST['ct'].split("\r\n")
                for txt in lsplit:
                    inp = txt
                    key = request.POST['key']
                    hexinp = ""
                    for i in inp:
                        hexinp += AES.toTxt(AES.toBin(i,8))
                    hexkey = ""
                    for i in key:
                        hexkey += AES.toTxt(AES.toBin(i,8))
                    dec_out = AES.decrypt(hexinp,hexkey)
                    txt = ""
                    for i in dec_out:
                        txt += AES.toBin(i)
                    fin = AES.toTxt(txt,8)
                    it = -1
                    while (fin[it]==" "):
                        it -= 1
                    if (it==-1):
                        it = len(fin) - 1
                    fin = fin[:it+1]
                    dec.append(fin)
                form = AESForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                lsplit = request.POST['pt'].split("\r\n")
                for txt in lsplit:
                    inp = txt
                    key = request.POST['key']
                    if (len(inp)%16!=0):
                        inp += " " * (16 - (len(inp) % 16))
                    hexinp = ""
                    for i in inp:
                        hexinp += AES.toTxt(AES.toBin(i,8))
                    hexkey = ""
                    for i in key:
                        hexkey += AES.toTxt(AES.toBin(i,8))
                    enc_out = AES.encrypt(hexinp,hexkey)
                    print(enc_out)
                    txt = ""
                    for i in enc_out:
                        txt += AES.toBin(i)
                    enc.append(AES.toTxt(txt,8))
                form = AESForm(request.POST)
            return render(request, "aes.html", {"form":form, "error":error, "extra":extra, "enc":enc, "dec":dec})
    else:
        form = AESForm()
    return render(request,"aes.html",{"form":form})

def diffieHellman(request):
    if request.method == "POST":
        form = DFForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            apub = ""
            bpub = ""
            result = ""
            isPrime = True
            for i in range(2,int(request.POST['q'])):
                if (int(request.POST['q'])%i==0):
                    isPrime = False
                    break
            if (not isPrime):
                error = "The entered number is not a Prime Number"
            elif (int(request.POST.get("a")) not in DiffieHellman.primitiveRoot(int(request.POST['q']))):
                error = request.POST['a'] + " is not a primitive root of " + request.POST['q'] + ". Please enter one of the following values: " + str(DiffieHellman.primitiveRoot(int(request.POST['q'])))
            elif (int(request.POST['xa'])>=int(request.POST['q']) or int(request.POST['xa'])>=int(request.POST['q'])):
                error = "Both Private Keys have to be lesser than the Prime Number"
            else:
                inp = int(request.POST['q'])
                root = int(request.POST['a'])
                xa = int(request.POST['xa'])
                xb = int(request.POST['xb'])
                apub = (root ** xa) % inp
                bpub = (root ** xb) % inp
                ka = (bpub ** xa) % inp
                kb = (apub ** xb) % inp
                if (ka == kb):
                    result = "Key Successfully Generated : " + str(ka)
                else:
                    result = "Key Generation Algorithm Failed!"
                form = DFForm(request.POST)
            return render(request, "diffie-hellman.html", {"form":form, "error":error, "extra":extra, "apub":apub, "bpub":bpub, "result":result})
    else:
        form = DFForm()
    return render(request,"diffie-hellman.html",{"form":form})

def elGamal(request):
    if request.method == "POST":
        form = ElGamalForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            result = ""
            sign = ""
            isPrime = True
            for i in range(2,int(request.POST['q'])):
                if (int(request.POST['q'])%i==0):
                    isPrime = False
                    break
            if (not isPrime):
                error = "The entered number is not a Prime Number"
            elif (int(request.POST.get("a")) not in ElGamal.primitiveRoot(int(request.POST['q']))):
                error = request.POST['a'] + " is not a primitive root of " + request.POST['q'] + ". Please enter one of the following values: " + str(DiffieHellman.primitiveRoot(int(request.POST['q'])))
            elif (request.POST['verify']=="" and request.POST['xa']==""):
                error = "Kindly enter the Signature / Private Key, to Verify / Sign the message"
            elif (request.POST['verify']=="" and request.POST['k']==""):
                error = "Kindly enter the Signature / Random No., to Verify / Sign the message"
            else:
                inp = int(request.POST['q'])
                root = int(request.POST['a'])
                priv = int(request.POST['xa'])
                pub = (root ** priv) % inp
                msg = request.POST['m']
                hs = int(hashlib.md5(msg.encode()).hexdigest(),16)%100000
                rnd = int(request.POST['k'])
                ki = ElGamal.inverse(rnd,inp-1)
                if (request.POST['verify']==""):
                    s1 = (root ** rnd) % inp
                    s2 = (ki * (hs - (priv * s1))) % (inp - 1)
                    result = "Digital Signature Generated:"
                    sign = "[" + str(s1) + ", " + str(s2) + "]"
                else:
                    temp = request.POST['verify'].replace(" ","")
                    sig = temp[1:-1].split(",")
                    v1 = (root ** hs) % inp
                    v2 = ((pub ** int(sig[0])) * (int(sig[0]) ** int(sig[1]))) % inp
                    if (v1 == v2):
                        result = "Digital Signature Verified Successfully!"
                    else:
                        result = "Verification Failed! Signs don't Match"
                form = ElGamalForm(request.POST)
            return render(request, "el-gamal.html", {"form":form, "error":error, "extra":extra, "result":result,"sign":sign})
    else:
        form = ElGamalForm()
    return render(request,"el-gamal.html",{"form":form})

def rsa(request):
    if request.method == "POST":
        form = RSAForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            ret_p = ""
            ret_q = ""
            ret_n = ""
            ret_phi = ""
            ret_enc = []
            ret_dec = []
            request.POST._mutable = True
            chs = [4,8,16,32,64,128,256,512,1024,2048,4096]
            if int(request.POST['b']) not in chs:
                error = "The input for no. of bits is not one of the given choices"
            elif (request.POST['m']=="" and request.POST['enc']==""):
                error = "Please enter a Message / Encrypted Text to perform Encryption / Decryption"
            else:
                if (request.POST['p']=="" and request.POST['q']==""):
                    p = RSA.primeGen(int(request.POST['b']))
                    q = p
                    while (q==p):
                        q = RSA.primeGen(int(request.POST['b']))
                    request.POST['p'] = str(p)
                    request.POST['q'] = str(q)
                else:
                    p = int(request.POST['p'])
                    q = int(request.POST['q'])
                n = p * q
                phi = (p - 1) * (q - 1)
                if (request.POST['e']!="" and math.gcd(phi,int(request.POST['e']))!=1):
                    error = "The given encryption key is not coprime with the generated value of phi. Kindly flag the field to allow generating the key"
                else:
                    if (request.POST['e']==""):
                        e = random.randint(2,phi-1)
                        while(math.gcd(phi,e)!=1):
                            e = random.randint(2,phi-1)
                        request.POST['e'] = e
                    else:
                        e = int(request.POST['e'])
                    d = RSA.inverse(e,phi)
                    exp = 0
                    numtxt = str(e)
                    for i in range(len(numtxt)):
                        exp = ((exp * 10 + ord(numtxt[i]) - 48) % (n - 1))
                    dexp = 0
                    dnumtxt = str(d)
                    for i in range(len(dnumtxt)):
                        dexp = ((dexp * 10 + ord(dnumtxt[i]) - 48) % (n - 1))
                    if (request.POST['m']!=""):
                        lsplit = request.POST['m'].split("\r\n")
                        for txt in lsplit:
                            temp = []
                            for i in txt:
                                temp.append(RSA.power(ord(i),exp,n))
                            enc = ""
                            for i in temp:
                                enc += str(i) + ", "
                            ret_enc.append(enc[:-2])
                    else:
                        lsplit = request.POST['enc'].split("\r\n")
                        for txt in lsplit:
                            temp = []
                            spl = txt.replace(" ","").split(",")
                            for i in spl:
                                temp.append(RSA.power(int(i),dexp,n))
                            dec = ""
                            for i in temp:
                                dec += chr(i)
                            ret_dec.append(dec)

                ret_p = str(p)
                ret_q = str(q)
                ret_n = str(n)
                ret_phi = str(phi)
            form = RSAForm(request.POST)
            return render(request,"rsa.html",{"form":form, "error" : error, "extra" : extra, "p":ret_p, "q":ret_q, "n":ret_n, "phi":ret_phi, "enc":ret_enc, "dec":ret_dec})
    else:
        form = RSAForm()
    return render(request,"rsa.html",{"form":form})