from django.http import HttpResponse
from django.shortcuts import render,redirect


def homepage(request):
    if request.user.is_authenticated:
          return redirect('myhome')
    return render(request,"login/index.html",{})

def mylogin(request):
        return HttpResponse("login Here!!!")
