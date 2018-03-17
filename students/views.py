from django.shortcuts import render,redirect
from django.urls import reverse

from .models import Student

# Create your views here.
def index(request):
    return render(request,'students/index.html')
def list(request):
    students_list = Student.objects.all()
    # return redirect(reverse('students:detail',args = [1]))
    # return redirect(reverse('students:detail', kwargs={'id':3}))
    # return redirect(reverse('students:index'))
    return render(request,'students/list.html',{'list':students_list})
def detail(request,id):
    student = Student.objects.get(id=id)
    return render(request,'students/detail.html',{'student':student})