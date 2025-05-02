from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import userpost
from .forms import userpoststatus



# Create your views here.
def landing(request):
    posts=userpost.objects.all().order_by('-created_at')
    return render(request,"login/feed.html",{'posts':posts})

def logout_session(request):
    logout(request)
    return redirect('myhome')


def deletePost(request):
    d_id=request.POST.get('post_id')
    userpost.objects.get(post_id=d_id).delete()
    return redirect('myposts')


def postuser(request):
    if request.method == 'POST':
        form = userpoststatus(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myhome')
        
def myposts(request):
    myusername =request.user.username
    posts = userpost.objects.filter(user_name=myusername)

    # return HttpResponse (posts)
    return render(request,"login/mypost.html",{'posts':posts})      
        
    
                  
            

def login_auth(request):
    if request.method =='POST':
        f_user=request.POST['username']
        f_pass=request.POST['password']
        user=authenticate(request,username=f_user,password=f_pass)
        if user is not None:
            login(request,user)
            return render(request,"login/home.html",{'name':user.username})
        else:
            return redirect('home')
    

    

