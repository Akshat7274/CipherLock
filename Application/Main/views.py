import random
from django.shortcuts import render
from Ciphers import Caesar, Playfair, Hill, Vigenere, Vernam, Railfence, RailfenceNew, RCTransform, DES, AES, DiffieHellman
from .forms import CaesarForm, PlayfairForm, HillForm, VigenereForm, VernamForm, RailfenceForm, RCTForm, DESForm, AESForm, DFForm
import math

# Create your views here.

def index(request):
    return render(request,'index.html')

def caesar(request):
    if request.method == "POST":
        form = CaesarForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                request.POST['pt'] = Caesar.decrypt(request.POST['ct'],int(request.POST['key']))
                form = CaesarForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                request.POST['ct'] = Caesar.encrypt(request.POST['pt'],int(request.POST['key']))
                form = CaesarForm(request.POST)
            return render(request, "caesar.html", {"form":form, "error":error, "extra":extra})
    else:
        form = CaesarForm()
    return render(request,"caesar.html",{"form":form})

def playfair(request):
    if request.method == "POST":
        form = PlayfairForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                spText = request.POST['ct'].split(" ")
                request.POST['pt'] = ""
                for i in spText:
                    request.POST['pt'] += Playfair.rejoin(Playfair.decrypt(i,Playfair.key_matrix(request.POST['key']))) + " "
                request.POST['pt'] = request.POST['pt'][0:-1]
                form = PlayfairForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                spText = request.POST['pt'].split(" ")
                request.POST['ct'] = ""
                for i in spText:
                    request.POST['ct'] += Playfair.encrypt(Playfair.txtsplit(i),Playfair.key_matrix(request.POST['key'])) + " "
                request.POST['ct'] = request.POST['ct'][0:-1]
                form = PlayfairForm(request.POST)
            return render(request, "playfair.html", {"form":form, "error":error, "extra":extra})
    else:
        form = PlayfairForm()
    return render(request,"playfair.html",{"form":form})

def hill(request):
    if request.method == "POST":
        form = HillForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            l = len(request.POST['key'])
            if (math.sqrt(l)!=int(math.sqrt(l))):
                error = "The entered key is not valid! Kindly enter an NxN key"
            elif (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                request.POST['pt'] = ""
                for i in request.POST['ct'].split(" "):
                    response = Hill.decrypt(i,request.POST['key'],l)
                    for i in response:
                        if (i.islower()):
                            request.POST['pt'] += i
                    request.POST['pt'] += " "
                request.POST['pt'] = request.POST['pt'][0:-1]
                form = HillForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                request.POST['ct'] = ""
                for i in request.POST['pt'].split(" "):
                    request.POST['ct'] += Hill.encrpyt(i,request.POST['key'],l) + " "
                request.POST['ct'] = request.POST['ct'][0:-1]
                form = HillForm(request.POST)
            return render(request, "hill.html", {"form":form, "error":error, "extra":extra})
    else:
        form = HillForm()
    return render(request,"hill.html",{"form":form})

def vigenere(request):
    if request.method == "POST":
        form = VigenereForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                request.POST['pt'] = Vigenere.decrypt(request.POST['ct'],request.POST['key'])[-1][-1]
                form = VigenereForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                request.POST['ct'] = Vigenere.encrypt(request.POST['pt'],request.POST['key'])[-1][-1]
                form = VigenereForm(request.POST)
            return render(request, "vigenere.html", {"form":form, "error":error, "extra":extra})
    else:
        form = VigenereForm()
    return render(request,"vigenere.html",{"form":form})

def vernam(request):
    if request.method == "POST":
        form = VernamForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                request.POST['pt'] = ""
                for i in request.POST['ct'].split(" "):
                    request.POST['pt'] += Vernam.txtcvt(Vernam.xoring(Vernam.binary(i),Vernam.binary(request.POST['key']))) + " "
                request.POST['pt'] = request.POST['pt'][0:-1]
                form = VernamForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                request.POST['ct'] = ""
                for i in request.POST['pt'].split(" "):
                    request.POST['ct'] += Vernam.txtcvt(Vernam.xoring(Vernam.binary(i),Vernam.binary(request.POST['key']))) + " "
                request.POST['ct'] = request.POST['ct'][0:-1]
                form = VernamForm(request.POST)
            return render(request, "vernam.html", {"form":form, "error":error, "extra":extra})
    else:
        form = VernamForm()
    return render(request,"vernam.html",{"form":form})

def railfence(request):
    if request.method == "POST":
        form = RailfenceForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                request.POST['pt'] = Railfence.decrypt(request.POST['ct'],int(request.POST['key']))
                form = RailfenceForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                request.POST['ct'] = Railfence.encrypt(request.POST['pt'],int(request.POST['key']))
                form = RailfenceForm(request.POST)
            return render(request, "railfence-conv.html", {"form":form, "error":error, "extra":extra})
    else:
        form = RailfenceForm()
    return render(request,"railfence-conv.html",{"form":form})

def railfenceNew(request):
    if request.method == "POST":
        form = RailfenceForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                request.POST['pt'] = RailfenceNew.decrypt(request.POST['ct'],int(request.POST['key']))
                form = RailfenceForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                request.POST['ct'] = RailfenceNew.encrypt(request.POST['pt'],int(request.POST['key']))
                form = RailfenceForm(request.POST)
            return render(request, "railfence-new.html", {"form":form, "error":error, "extra":extra})
    else:
        form = RailfenceForm()
    return render(request,"railfence-new.html",{"form":form})

def rcTransform(request):
    if request.method == "POST":
        form = RCTForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                request.POST['pt'] = RCTransform.decrypt(request.POST['ct'],request.POST['key'])
                form = RCTForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                request.POST['ct'] = RCTransform.encrypt(request.POST['pt'],request.POST['key'])
                form = RCTForm(request.POST)
            return render(request, "rc-transform.html", {"form":form, "error":error, "extra":extra})
    else:
        form = RCTForm()
    return render(request,"rc-transform.html",{"form":form})

def des(request):
    if request.method == "POST":
        form = DESForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                inp = request.POST['ct']
                key = request.POST['key']
                hexinp = ""
                for i in inp:
                    hexinp += DES.toTxt(DES.toBin(i,8))
                hexkey = ""
                for i in key:
                    hexkey += DES.toTxt(DES.toBin(i,8))
                dec = DES.decrypt(hexinp,hexkey)
                txt = ""
                for i in dec:
                    txt += DES.toBin(i)
                fin = DES.toTxt(txt,8)
                it = -1
                while (fin[it]==" "):
                    it -= 1
                if (it==-1):
                    it = len(fin) - 1
                fin = fin[:it+1]
                request.POST['pt'] = fin
                form = DESForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                inp = request.POST['pt']
                key = request.POST['key']
                if (len(inp)%8!=0):
                    inp += " " * (8 - (len(inp) % 8))
                hexinp = ""
                for i in inp:
                    hexinp += DES.toTxt(DES.toBin(i,8))
                hexkey = ""
                for i in key:
                    hexkey += DES.toTxt(DES.toBin(i,8))
                enc = DES.encrypt(hexinp,hexkey)
                txt = ""
                for i in enc:
                    txt += DES.toBin(i)
                request.POST['ct'] = DES.toTxt(txt,8)
                form = DESForm(request.POST)
            return render(request, "des.html", {"form":form, "error":error, "extra":extra})
    else:
        form = DESForm()
    return render(request,"des.html",{"form":form})

def aes(request):
    if request.method == "POST":
        form = AESForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            if (request.POST.get("pt")=="" and request.POST.get("ct")==""):
                error = "Please enter a Plaintext / Ciphertext to perform Encryption / Decryption"
            elif (request.POST.get("pt")==""):
                extra = "Explanation of Decryption"
                inp = request.POST['ct']
                key = request.POST['key']
                hexinp = ""
                for i in inp:
                    hexinp += AES.toTxt(AES.toBin(i,8))
                hexkey = ""
                for i in key:
                    hexkey += AES.toTxt(AES.toBin(i,8))
                dec = AES.decrypt(hexinp,hexkey)
                txt = ""
                for i in dec:
                    txt += AES.toBin(i)
                fin = AES.toTxt(txt,8)
                it = -1
                while (fin[it]==" "):
                    it -= 1
                if (it==-1):
                    it = len(fin) - 1
                fin = fin[:it+1]
                request.POST['pt'] = fin
                form = AESForm(request.POST)
            elif (request.POST.get("ct")==""):
                extra = "Explanation of Encryption"
                inp = request.POST['pt']
                key = request.POST['key']
                if (len(inp)%16!=0):
                    inp += " " * (16 - (len(inp) % 16))
                hexinp = ""
                for i in inp:
                    hexinp += AES.toTxt(AES.toBin(i,8))
                hexkey = ""
                for i in key:
                    hexkey += AES.toTxt(AES.toBin(i,8))
                enc = AES.encrypt(hexinp,hexkey)
                txt = ""
                for i in enc:
                    txt += AES.toBin(i)
                request.POST['ct'] = AES.toTxt(txt,8)
                form = AESForm(request.POST)
            return render(request, "aes.html", {"form":form, "error":error, "extra":extra})
    else:
        form = AESForm()
    return render(request,"aes.html",{"form":form})

def diffieHellman(request):
    if request.method == "POST":
        form = DFForm(request.POST)
        if form.is_valid():
            error = ""
            extra = ""
            request.POST._mutable = True
            isPrime = True
            for i in range(2,int(request.POST['q'])):
                if (int(request.POST['q'])%i==0):
                    isPrime = False
                    break
            if (not isPrime):
                error = "The entered number is not a Prime Number"
            elif (int(request.POST.get("a")) not in DiffieHellman.primitiveRoot(int(request.POST['q']))):
                error = request.POST['a'] + " is not a primitive root of " + request.POST['q'] + ". Please enter one of the following values: " + str(DiffieHellman.primitiveRoot(int(request.POST['q'])))
            else:
                extra = "Explanation of Encryption"
                inp = int(request.POST['q'])
                root = int(request.POST['a'])
                request.POST['xa'] = random.randint(2,inp-1)
                request.POST['xb'] = request.POST['xa']
                while (request.POST['xb'] == request.POST['xa']):
                    request.POST['xb'] = random.randint(2,inp-1)
                request.POST['ya'] = (root ** request.POST['xa']) % inp
                request.POST['yb'] = (root ** request.POST['xb']) % inp
                ka = (request.POST['yb'] ** request.POST['xa']) % inp
                kb = (request.POST['ya'] ** request.POST['xb']) % inp
                if (ka == kb):
                    request.POST['key'] = ka
                else:
                    request.POST['key'] = "Failed"
                form = DFForm(request.POST)
            return render(request, "diffie-hellman.html", {"form":form, "error":error, "extra":extra})
    else:
        form = DFForm()
    return render(request,"diffie-hellman.html",{"form":form})