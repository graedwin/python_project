from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'logout$', views.logout),
    url(r'newUser$', views.newuser),
    url(r'existingUser$', views.existinguser),
    url(r'edit_user_form$', views.edit_user_form),
    url(r'edit_user$', views.edit_user),

]