from django.shortcuts import render
from django.http import HttpResponse

def virat(request):
    return render(request,'virat.html')
# Create your views here.
def maxwell(request):
    return HttpResponse("sixer")
