from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article

# Create your views here.


# http test-------------------

# def home(request):
#     return HttpResponse("hello world")

# ----------------------------

# these are Json tests --------------------------------------


# def api(request):
#     return JsonResponse({"Title": "سلام دنیا"})

# def api(request):
#     data = {
#         "1": {
#             "title": "مقاله اول",
#             "id": 20,
#             "slug": "first article"
#         },

#         "2": {
#             "title": "مقاله دوم",
#             "id": 21,
#             "slug": "second article"
#         }

#     }
#     return JsonResponse(data)


#------------------------------------------------------------


# def home(request):

#     context = {
#         "articles":[
#             {
#             "username": "Amin",
#             "age": 24,
#             "job": "Programer",
#             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1920px-Google_2015_logo.svg.png"
#             },
#             {
#             "username": "Alireza",
#             "age": 24,
#             "job": "Programer",
#             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1920px-Google_2015_logo.svg.png"
#             },
#         ]
        
#     }

#     return render(request, "blog/home.html", context)






def home(request):

    context = {
        # "articles": Article.objects.all()
        "articles": Article.objects.filter(status='p').order_by('-publish') # [:2] #bracket shows number of articles that we want to show
    }

    return render(request, "blog/home.html", context)

def detail(request, slug):

    context = {
        # "articles": Article.objects.all()
        # "article": Article.objects.get(slug=slug)
        "article": get_object_or_404(Article, slug=slug, status="p")
    }

    return render(request, "blog/detail.html", context)

