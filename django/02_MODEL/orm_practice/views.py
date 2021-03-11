from django.shortcuts import render, redirect
from .models import Student

# Retrieve / Read (조회)
def index(request):
    students = Student.objects.all()
    s = Student.objects.get(id=1)
    context = {
        'students': students,
    }
    return render(request, 'orm_practice/index.html', context)

## 단일 조회
def detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'orm_practice/detail.html', context)


# Create (생성)
## html 제공
def new(request):
    return render(request, 'orm_practice/new.html')

#실제 저장
def create(request):
    student = Student()
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.intro = request.GET.get('intro')
    student.save()
    # redirect(RAW URL / urls.py 의 name)
    return redirect('detail', pk=student.pk)

def edit(request, pk):
    student = Student.objects.get(pk=pk)
    context ={ 'student' :student }
    return render(request, 'orm_practice/detail.html', context )

def update(request, pk):
    student = Student.objects.get(pk=pk)
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.intro = request.GET.get('intro')
    student.save()
    
    return redirect('detail', pk=student.pk)

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('index')
