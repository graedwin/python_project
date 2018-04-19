from django.shortcuts import render,redirect
from ..login_and_registration.models import *
from models import *


def index(request):
    return render(request,'instadraw/index.html',{'posts':Post.objects.all()})

def logout(request):
    request.session.clear()
    return redirect('/welcome')

def new_post(request):
    return render(request,'instadraw/create_post.html')

def profile(request):
    id=request.session['user_id']
    context = {
        "my_post" : User.objects.get(id=id).posts.all(),
        "user" : User.objects.get(id=id).username,
    }
    return render(request,'instadraw/profile.html',context)
   
def save(request):
    Post.objects.create(pic=request.POST['image'],posted_by=User.objects.get(id=request.session['user_id']),description=request.POST['description'])
    return redirect('/instadraw')