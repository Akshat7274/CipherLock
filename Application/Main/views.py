from django.http import QueryDict
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Ciphers import Caesar, Playfair
from .forms import CaesarForm, PlayfairForm

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