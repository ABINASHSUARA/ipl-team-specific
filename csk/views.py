from django.shortcuts import render
from django.http import HttpResponse


def dhoni(request):
    return render(request,'dhoni.html')
# Create your views here.
def raina(request):
    return HttpResponse("mr ipl")