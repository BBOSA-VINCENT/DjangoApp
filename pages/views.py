from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    context={'rooms':rooms}
    return render(request,'contact.html',context)

def numbers(request):
    return render(request,'numbers.html',{'rooms':rooms})

rooms=[
    {'id':1,'name':'BBOSA'},
    {'id':2,'name':'Vincent'},
    {'id':3,'name':'PrinceVince'}
]