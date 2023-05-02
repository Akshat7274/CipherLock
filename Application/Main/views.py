from django.shortcuts import render
from Ciphers import Caesar, Playfair, Hill, Vigenere, Vernam
from .forms import CaesarForm, PlayfairForm, HillForm, VigenereForm, VernamForm
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