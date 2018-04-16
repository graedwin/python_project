from django.shortcuts import render,redirect
from ..login_and_registration.models import *


def index(request):
    return render(request, 'instadraw/index.html')
def logout(request):
    request.session.clear()
    return redirect('/dashboard')