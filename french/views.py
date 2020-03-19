from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import French
# Create your views here.
def home(request):
    return render(request,'french/home.html')

def franchise(request):
    franchises = French.objects.all()
    return render(request,'french/franchise.html',{'franchises':franchises})

def display(request,fr_id):
    display = get_object_or_404(French,pk=fr_id)
    print(display)
    return render(request,'french/display.html',{'display':display})