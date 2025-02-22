from django.shortcuts import render, HttpResponse

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
        'articles': Article.objects.all()
    }
    return render(request, 'dashboard.html', context)

def create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'createarticle.html', context)

def article(request, id):
    context = {
        'article': Article.objects.get(id=id)
    }
    return render(request, 'article.html', context)
