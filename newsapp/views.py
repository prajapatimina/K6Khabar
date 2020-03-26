from django.shortcuts import render
from .models import PostModel,CategoryModel
import datetime 

# def index(request):
#     posts = PostModel.objects.all()
    
#     context= {
#         'posts': posts
#     }
#     return render(request, 'newsapp/index.html', context)

    
def index(request):
    #sports_category = CategoryModel.objects.filter(name='Sports').first()


    # categories = CategoryModel.objects.filter(name='Sports')
    # sports_category= None
    # for category in categories:
    #     sports_category = category

  #  posts= PostModel.objects.filter(posted_on__gte = datetime.date(2020, 3, 20))

    # sports_category = CategoryModel.objects.filter(name='Sports').first()
    # posts= PostModel.objects.exclude(title__startswith='A').filter(category=sports_category)

    posts = PostModel.objects.all()[:10]
    categories= CategoryModel.objects.all()[:5]
    featured_post = posts[0]
    context={
        'posts': posts,
        'categories': categories,
        'featured_post': featured_post

    }
    return render(request, 'newsapp/index.html', context)


def detail(request,id):
    post = PostModel.objects.filter(id=id).first()
    categories= CategoryModel.objects.all()[:5]
    context ={
        'posts':post,
        'categories': categories,

    }
    return render(request,'newsapp/detail.html',context)

def categorynews(request, id):
    category = CategoryModel.objects.filter(id=id).first()
    categories= CategoryModel.objects.all()[:5]
    
    if category:
        posts =PostModel.objects.filter(category=category)
        
        # featured_post =posts[0]
        context ={
            'posts':posts,
            'categories': categories,
            # 'featured_post': featured_post

        }
        return render(request, 'newsapp/index.html',context)
    else:
        return render(request,'newsapp/error404.html')

