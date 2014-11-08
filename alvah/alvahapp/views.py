from django.shortcuts import render

from mezzanine.blog.models import BlogPost, BlogCategory
# Create your views here.

def home(request):

    blog_posts = BlogPost.objects.published(for_user=request.user).all()
    default_images = ['static/img/default_drawing1.jpg','static/img/default_drawing2.jpg']
    context = {'blog_posts': blog_posts,
               'default_images':default_images,
                }
    return render(request, 'index.html', context)
