from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle

def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'articles/article_list.html',{'articles': articles})


def article_detail(request,slug_take):
    article = Article.objects.get(slug=slug_take)
    return render(request, 'articles/article_detail.html', {'article' : article})

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method =='POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})