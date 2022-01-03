from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.db.models import Q
from .models import Article, Category
from .forms import ArticleForm

def index(request):

    data = Article.objects.filter(state=1)
    categories = Category.objects.filter(state=1)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context= {
        "articles" : page_obj,
        "categories" : categories
    }
    return render(request, "blog/index.html", context)

def show(request, slug):

    my_article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/show.html",{
        "article" : my_article
    })

def create(request):
    form = ArticleForm

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("articles_list")
    return render(request, 'blog/create.html', {"form" : form})


def edit(request, id):

    article = Article.objects.get(pk=id)
    form = ArticleForm(instance=article)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect("articles_list")
    

    return render(request, 'blog/edit.html', {"form" : form})

def delete(request, id):
    obj = get_object_or_404(Article, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("articles_list")

def search_posts(request):
    query = request.GET.get('search')
    articles = Article.objects.filter( Q(title__icontains=query) | Q(description__icontains=query) | Q(picture__icontains=query))
    # paginator = Paginator(articles, 3)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        "articles":articles,
        "q":query
    }
    return render(request, 'blog/search_posts.html', context)