from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^', include("apps.login_and_registration.urls")),
    url(r'^dashboard$', include("apps.instadraw.urls")),
]
