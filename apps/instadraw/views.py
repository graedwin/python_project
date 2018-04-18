from django.shortcuts import render,redirect
from ..login_and_registration.models import *
from django.contrib import messages
from models import *


def index(request):
    if not 'user_id' in request.session:
        return render(request, 'login_and_registration_app/index.html')
    else:
        return render(request,'instadraw/index.html',{'posts':Post.objects.all()})
def logout(request):
    request.session.clear()
    return redirect('/welcome')
def new_post(request):
    return render(request,'instadraw/create_post.html')
def save(request):
    errors= Post.objects.validate_canvas(request.POST['image'])
    if errors[0]:
        Post.objects.create(pic=request.POST['image'],posted_by=User.objects.get(id=request.session['user_id']),description=request.POST['description'])
        return redirect('/instadraw')
    else:
        messages.add_message(request, messages.INFO, errors[1])
        return redirect('/instadraw/create_post')
        