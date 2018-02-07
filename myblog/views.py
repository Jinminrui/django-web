from django.shortcuts import render, render_to_response
from django.http import Http404

# Create your views here.
from myblog.models import BlogPost


def myBlogs(request):
    blog_list = BlogPost.objects.all()
    return render_to_response('BlogTemplate.html',{'blog_list':blog_list})

def get_details(request,blog_id):
    try:
        blog = BlogPost.objects.get(id = blog_id)
    except:
        raise Http404
    ctx = {
        'blog':blog
    }

    return render(request,'blog_details.html',ctx)




