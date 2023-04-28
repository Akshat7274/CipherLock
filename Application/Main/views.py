from django.http import QueryDict
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Ciphers import Caesar
from .forms import CaesarForm

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
            print(form)
            return render(request, "caesar.html", {"form":form, "error":error, "extra":extra})
    else:
        form = CaesarForm()
    return render(request,"caesar.html",{"form":form})