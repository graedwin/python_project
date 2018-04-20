from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
import json
from ..login_and_registration.models import *
from django.contrib import messages
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
        "posts" : User.objects.get(id=id).posts.all(),
    }
    return render(request,'instadraw/profile.html',context)
   
def save(request):
    Post.objects.create(pic=request.POST['image'],posted_by=User.objects.get(id=request.session['user_id']),description=request.POST['description'])
    return redirect('/instadraw')

def show (request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post_id': post.id,
        'description': post.description,
        'pic': post.pic,
        'posted_by': post.posted_by,
        'created_at': post.created_at,
        'likes_total': post.liked_by.count(),
        'comments_total': post.comments.count(),
        'comments': post.comments.all().order_by('-created_at')
    }

    return render (request, 'instadraw/show.html', context)
    
def like(request, post_id):
    print '-----> POST_ID: ', post_id

    user = User.objects.get(id=request.session['user_id'])
    post = Post.objects.get(id=post_id)
    
    if user not in post.liked_by.all():
        post.liked_by.add(user)
    else:
        post.liked_by.remove(user)
    dictionary = {
        'response': post.liked_by.count()
    }
    return HttpResponse(json.dumps(dictionary), content_type='application/json')

    #return redirect ('/instadraw/show/'+str(post_id))

def add_comment (request, post_id):
    post = Post.objects.get(id=post_id)
    user = User.objects.get(id=request.session['user_id'])
    postData = {
        'post': post,
        'user': user,
        'content': request.POST['content']
    }
    new_comment = Comment.objects.commentValidator (postData)

    if not new_comment[0]:
        messages.error(request, new_comment[1])

    return redirect ('/instadraw/show/'+str(post_id))

def delete_comment (request, post_id, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect ('/instadraw/show/'+str(post_id))


def search (request):
    search_results = Post.objects.filter(description__contains=request.POST['search'])
    print search_results

    return render (request, 'instadraw/search_results.html', { 'search_results': search_results} )
    
#will only show up if session['user_id'] matches the post's uploaded_by
def edit_description (request, post_id):
    post = Post.objects.get(id=post_id)
    post.description=request.POST['description']
    post.save() 
    return redirect('/instadraw')

def delete_post (request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('/instadraw')
    
