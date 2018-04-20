# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    if not 'user_id' in request.session:
        return render(request, 'login_and_registration_app/index.html')
    else:
        return redirect('/instadraw')

def register(request):
    print request.POST
    result = User.objects.validate_reg(request.POST) # (False, [' ', ' '])
    if result[0]:
        # True and we have a new user
        request.session['user_id'] = result[1].id
        request.session['user_name'] = result[1].first_name
        return redirect('/instadraw')
    else:
        # False and we have errors to show
        for error in result[1]: # my errors list ['first name required', 'last name required']
            messages.add_message(request, messages.INFO, error)

        return redirect('/welcome/newUser')

def login(request):
    result = User.objects.validate_log(request.POST)
    if result[0]:
        # True and we have a new user
        request.session['user_id'] = result[1].id
        request.session['user_name'] = result[1].first_name
        return redirect('/instadraw')
    else:
        # False and we have errors to show
        for error in result[1]: # my errors list ['first name required', 'last name required']
            messages.add_message(request, messages.INFO, error)
        return redirect('/welcome')
        
def logout(request):
    request.session.clear()
    return redirect('/welcome')
def newuser(request):
    return render(request, 'login_and_registration_app/register.html')
def existinguser(request):
    return render(request, 'login_and_registration_app/index.html')

def edit_user_form (request):
    user = User.objects.get(id=request.session['user_id'])
    return render (request, 'login_and_registration_app/edit_user_form.html', { 'user': user})

def edit_user (request):
    
    result = User.objects.validate_reg(request.POST, request.session['user_id'])

    if not result[0]:
        for error in result[1]:
            messages.error (request, error)
        return redirect ('/welcome/edit_user_form')
    return redirect ('/instadraw/profile')

