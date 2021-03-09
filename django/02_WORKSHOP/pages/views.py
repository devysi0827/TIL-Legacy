from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def dinner(request,menu,people):

    context = {
        'menu': menu,
        'people': people,
    }

    return render(request, 'dinner.html', context)