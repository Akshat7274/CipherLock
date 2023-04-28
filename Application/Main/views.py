from django.http import QueryDict
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Ciphers import Caesar
from .forms import NameForm, CaesarForm

# Create your views here.

def index(request):
    context = {
        'input' : Caesar.encrypt("Akshat",5),
        'check' : [[0,1,2],[3,4,5],[6,7,8]]
    }
    return render(request,'index.html',context)

def get_name(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = request.POST.get("your_name")
            return render(request, "name.html", {"form": form, "name" : name})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})

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