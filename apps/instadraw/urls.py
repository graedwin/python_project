from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
<<<<<<< HEAD
=======
    url(r'logout$', views.logout),
    url(r'profile', views.profile),
>>>>>>> changes
    url(r'create_post$', views.new_post),
    url(r'create_post/save$', views.save),
    url(r'^show/(?P<post_id>\d+)$', views.show),
    url(r'^add_comment/(?P<post_id>\d+)$', views.add_comment),
    url(r'^like/(?P<post_id>\d+)$', views.like),
    url(r'^search$', views.search),

]