from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Article

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template("MyApp/index.html")
    return HttpResponse(template.render(context, request))


def article(request):
    latest_article = Article.objects.all()
    template = loader.get_template("MyApp/article.html")
    context = {
        "latest_article_list": latest_article,
    }
    return HttpResponse(template.render(context, request))

def form(request):
    context = {}
    template = loader.get_template("MyApp/form.html")
    return HttpResponse(template.render(context, request))

