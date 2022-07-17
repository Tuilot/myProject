import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

from student.models import Student


def create(request):
    try:
        name = request.GET.get('name')
        score = request.GET.get('score')
        email = request.GET.get('email')

        stu = Student.objects.create(name=name, score=score, email=email)
        stu.save()
        return HttpResponse('create success!')
    except Exception as e:
        print(e)
        return HttpResponse("create fail!")


def get(request):
    students = Student.objects.all()
    students = list(students)
    result=[]
    for stu in students:
        result.append(stu.toJSON())
        print(stu.toJSON())
    print("----")
    return HttpResponse(result, "application/json")


def modify(request):
    try:
        my_id = request.GET.get('id')
        name = request.GET.get('name', default='')
        score = request.GET.get('score', default='')
        email = request.GET.get('email', default='')
        stu = Student.objects.filter(id=my_id)[0]
        if name != '':
            stu.name= name
        if score != '':
            stu.score = score
        if email != '':
            stu.email= email
        stu.save()
        return HttpResponse("modify success!")
    except Exception as e:
        print(e)
        return HttpResponse("modify fail!")
