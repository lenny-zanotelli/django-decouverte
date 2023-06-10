from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Article

# Create your views here.
def index(request):
    template = loader.get_template("MyApp/index.html")
    return HttpResponse(template.render(request))


def article(request):
    latest_article = Article.objects.all()
    template = loader.get_template("MyApp/article.html")
    context = {
        "latest_article_list": latest_article,
    }
    return HttpResponse(template.render(context, request))

