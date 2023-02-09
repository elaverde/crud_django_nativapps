from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from ..forms import StudentForm, RegistrationForm
from ..models import Student, Registration, Curse
def student_create(request):
    if request.method == 'GET':
        return render(request, 'students/create.html', {"form": StudentForm})
    else:
        form = StudentForm(request.POST)
        courses = request.POST.getlist('curse')
        if form.is_valid():
            student = form.save(commit=False)
            student.created_at = timezone.now()
            student.updated_at = timezone.now()
            student.save()
            #recorremos el array de id de cursos
            for curse_id in courses:
                curse = Curse.objects.get(id=curse_id)
                Registration.objects.create(student=student, curse=curse, created_at=timezone.now(), updated_at=timezone.now())
            return redirect('student_list')
        else:
            if not courses:
                return render(request, 'students/create.html', {"form": form, "error": "Debe seleccionar al menos un curso"})
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {"students": students})

def student_detail(request, id):
    if request.method == 'GET':
        student = get_object_or_404(Student, pk=id)
        registrations = Registration.objects.filter(student=student)
        courses = [registration.curse for registration in registrations]
        form = StudentForm(instance=student, initial={'curse': courses})
        return render(request, 'students/detail.html', {"student": student, "form": form})
    else:
        student = get_object_or_404(Student, pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.updated_at = timezone.now()
            student.save()
            # obtenemos el value del select multiple
            courses = request.POST.getlist('curse')
            # borramos todas las inscripciones previas
            Registration.objects.filter(student=student).delete()
            # recorremos el array de id de cursos
            for curse_id in courses:
                curse = Curse.objects.get(id=curse_id)
                Registration.objects.create(student=student, curse=curse, created_at=timezone.now(), updated_at=timezone.now())
            return redirect('student_list')
        else:
            print(form.errors)
def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('student_list')

def student_top_3(request):
    from datetime import datetime, timedelta
    today = datetime.now().date()
    six_months_ago = today - timedelta(days=180)
    registrations = Registration.objects.filter(created_at__gte=six_months_ago)
    from django.db.models import Count
    courses = registrations.values('curse').annotate(num_students=Count('student'))
    top_3_courses = courses.order_by('-num_students')[:3]
    courses_with_names = []
    for course in top_3_courses:
        curse_id = course['curse']
        curse = Curse.objects.get(id=curse_id)
        courses_with_names.append({
            'name': curse.name,
            'num_students': course['num_students']
        })
    return render(request, 'students/top_3.html', {"courses": courses_with_names})