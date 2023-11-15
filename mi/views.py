from django.shortcuts import render
from django.http import HttpResponse

def rohit(request):
    return render(request,'rohit.html')
# Create your views here.
def ishan(request):
    return HttpResponse("good keeper")
