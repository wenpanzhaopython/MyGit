import random

from django.http import HttpResponse
from django.shortcuts import render

from App.models import Person, Company, Grade, Student


def hello(request):
    return HttpResponse("Hello Django")

def helloT(request):
    return render(request, "helloDjango.html")

def person(request):

    persons = Person.objects.all()

    return render(request, "person.html", context={"persons":persons})

def companys(request):

    coms = Company.objects.all()

    return render(request, "companys.html", context={"companies":coms, "title":"公司de列表"})

def add_company(request):

    random_num = random.randint(6,30)

    name = "淘宝{num}".format(num=random_num)

    company = Company()

    company.name = name

    company.address = "天通苑{num}层".format(num=random_num)

    company.save()

    return HttpResponse(company.name)

def grade(request):

    grades = Grade.objects.all()

    return render(request, "grade.html", context={"grades":grades})

def student(request):

    students = Student.objects.all()

    return render(request, "student.html", context={"students":students})