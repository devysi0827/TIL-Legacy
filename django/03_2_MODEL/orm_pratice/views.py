from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
#조회
def index(request):
    s = Student.objects.get(id=1)
    age = s.id
   
    context = {
        'age' : age,
        
    }

    return render(request, 'orm_pratice/index.html', context)

def detail(request, pk):
    student =Student.objects.get(id=pk)
    name = student.name
    hobby = student.hobby
    context = {
        
        'name' : name,
        'hobby': hobby
    
    }
    return render(request, 'orm_pratice/detail.html', context)

#생성
def new(request):
    return render(request, 'orm_pratice/new.html')


def create(request):
    student = Student.objects.get(id=2)
    student.name = request.GET.get('title')
    student.hobby = request.GET.get('intro')
    student.save()

    return redirect('detail', pk=student.pk)