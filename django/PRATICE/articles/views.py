from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = { 'articles' : articles}
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('detail', pk= article.pk)
    elif request.method == 'GET':
        return redirect('new')
def edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)

def update(request,pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('detail', pk= article.pk)
    return redirect('edit', pk =pk)

def detail(request,pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html',context)

def delete(request, pk):
    if request.method == 'POST':

        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return redirect('index')
    return redirect('detail', pk =article.pk)
