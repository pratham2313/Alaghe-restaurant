from multiprocessing import context
from re import X
from django.shortcuts import render, HttpResponse
from datetime import datetime
from kali.models import Contact
from django.contrib import messages    # from messages django documentation

import kali

# Create your views here.


def index(request):
    context = {
        "x" : "hahahahahaha.",
        "y" : "Hello 2nd variable."
    }
    return render(request, 'test.html', context)
    # return HttpResponse("This is homepage of kali")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")
    

def punjabi(request):
    return render(request, 'punjabi.html')
    # return HttpResponse("This is book page from services section")

def south(request):
    return render(request, 'south.html')

def italian(request):
    return render(request, 'italian.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        # Popup after click submit
        messages.success(request, 'Submitted Successfully.')

    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")