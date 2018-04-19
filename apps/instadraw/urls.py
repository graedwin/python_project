from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'logout$', views.logout),
    url(r'profile', views.profile),
    url(r'create_post$', views.new_post),
    url(r'create_post/save$', views.save),
]