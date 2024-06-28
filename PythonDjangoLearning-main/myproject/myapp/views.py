from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Students
# Create your views here.

def index(request):
    return HttpResponse("Hello")

def render_view(request):
    return render(request, "myapp/index.html")

def student_form(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        Students.objects.create(first_name=first_name, last_name=last_name)
        return redirect("student_form")
    return render(request, "myapp/student.html")
    