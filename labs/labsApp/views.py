from django.shortcuts import render, get_object_or_404
from labsApp.models import Article

def home(request):
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def show_article(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    return render(request, 'article.html', {'article': article})