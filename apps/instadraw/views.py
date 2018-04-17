from django.shortcuts import render,redirect
from ..login_and_registration.models import *


def index(request):
    return render(request,'instadraw/index.html')
def logout(request):
    request.session.clear()
    return redirect('/dashboard')
def new_post(request):
    return render(request,'instadraw/create_post.html')
def save(request):
    x= request.POST
    print x
    print "Here"
    return redirect('/')