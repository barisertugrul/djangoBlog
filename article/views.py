from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from article.models import Article

from .forms import ArticleForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def dashboard(request):
    context = {
        'articles': Article.objects.filter(author = request.user)
    }
    return render(request, 'dashboard.html', context)

def create(request):
    form = ArticleForm(request.POST or None)
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
    context = {
        'article': Article.objects.filter(id=id, author=request.user).first()
    }
    return render(request, 'detail.html', context)

def update(request, id):
    pass

def delete(request, id):
    pass
