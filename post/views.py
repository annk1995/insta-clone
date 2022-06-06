from multiprocessing import context
from time import process_time_ns
from tokenize import group
from django.shortcuts import render
from post.models import Tag,Stream,Follow,Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    user =request.user
    posts = Stream.objects.filter(user=user)
    group_ids=[]
    for post in posts:
        group_ids.append(post.post_id)
        post_items =Post.objects.filter(id__in=group_ids).all().order_by('-posted ')
        context ={
            'post-items':post_items
        }
    return render(request,'index.html',context)