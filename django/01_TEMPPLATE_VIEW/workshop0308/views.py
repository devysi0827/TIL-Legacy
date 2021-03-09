from django.shortcuts import render
from django.http.response import HttpResponse
import random

# Create your views here.
def lotto(request):
    lotto = random.sample(range(1,46), 6)
    data = {
        'lotto' : sorted(lotto),
        'greeting' : 'hellow world!'
    }
    return render(request, 'workshop0308/lotto.html', data)
