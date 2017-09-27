from django.shortcuts import render,HttpResponse,redirect
from backapp import models
from django import forms
from django.forms import fields


def search_article(request,*args,**kwargs):
    article_type = models.ArticleType.objects.all()
    category = models.Category.objects.all()
    article = models.Article.objects.all().filter(article_type_id=2)
    print(request.path_info)
    return render(request,'back/search_article.html', {'article': article, 'article_type': article_type, 'category': category})