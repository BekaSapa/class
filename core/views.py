from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def homepage(request):
    return HttpResponse("hi")

def about(request):
    student = Student.objects.first()

    context = {
        "name": student.name,
        "address": student.address
    }

    rege = "about.html"
    return render(request, page, context)
    