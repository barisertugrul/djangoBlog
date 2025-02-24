from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from article.models import Article

from .forms import ArticleForm

# Create your views here.

def articles(request):
    keyword = request.GET.get('keyword')
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
    else:
        articles = Article.objects.all()

    context = {
        'articles': articles,
        'keyword': keyword
    }
    return render(request, 'articles.html', context)

def index(request):
    context = {}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

@login_required(login_url='user:login')
def dashboard(request):
    context = {
        'articles': Article.objects.filter(author = request.user)
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='user:login')
def create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Article created successfully')
        # form = ArticleForm()
        return redirect('article:dashboard')
    context = {
        'form': form
    }
    return render(request, 'createarticle.html', context)

def detail(request, id):
    """ context = {
        'article': Article.objects.filter(id=id, author=request.user).first()
    } """
    article = get_object_or_404(Article, id=id)
    context = {
        'article': article
    }
    return render(request, 'detail.html', context)

@login_required(login_url='user:login')
def update(request, id):
    """Update an article."""
    article = get_object_or_404(Article, id=id, author=request.user)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Article updated successfully')
        return redirect('article:dashboard')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)

@login_required(login_url='user:login')
def delete(request, id):
    """Delete an article."""
    article = get_object_or_404(Article, id=id, author=request.user)
    article.delete()
    messages.success(request, 'Article deleted successfully')
    return redirect('article:dashboard')
