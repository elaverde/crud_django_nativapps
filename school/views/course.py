from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from ..forms import CurseForm
from ..models import Curse

def create_course(request):
    if request.method == 'GET':
        return render(request, 'curses/create.html', {"form": CurseForm})
    else:
        form = CurseForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.created_at = timezone.now()
            curso.updated_at = timezone.now()
            curso.save()
            return redirect('course_list')
        else:
            print(form.errors)
            
def course_list(request):
    courses = Curse.objects.all()
    return render(request, 'curses/list.html', {"courses": courses})

def course_detail(request, id):
    if request.method == 'GET':
        course = get_object_or_404(Curse, pk=id)
        date_start = course.date_start.strftime('%Y-%m-%d')
        date_end = course.date_end.strftime('%Y-%m-%d')
        form = CurseForm(instance=course, initial={'date_start': date_start, 'date_end': date_end})
        return render(request, 'curses/detail.html', {"course": course, "form": form})
    else:
        course = get_object_or_404(Curse, pk=id)
        form = CurseForm(request.POST, instance=course)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.updated_at = timezone.now()
            curso.save()
            return redirect('course_list')
        else:
            print(form.errors)
def course_delete(request, id):
    course = get_object_or_404(Curse, pk=id)
    course.delete()
    return redirect('course_list')
