from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello I am in home")
     return render(request,'index.html')
def owner(request):
    return render(request,'owner.html')
def driver(request):
     return render(request,'driving.html')



