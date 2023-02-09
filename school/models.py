#from django.db import models
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellidos')
    age = models.IntegerField( verbose_name='Edad')
    email = models.EmailField( verbose_name='Correo')
    #curse = models.ManyToManyField("Curse", through='Registration' )
    curse = models.ManyToManyField("Curse", through='Registration', verbose_name='Cursos')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['id']
    def __str__(self):
        return 'Alumno: '+self.name+' '+self.last_name

class Curse(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    schedule = models.CharField(max_length=100, verbose_name='Horario')
    date_start = models.DateField( verbose_name='Fecha de inicio')
    date_end = models.DateField( verbose_name='Fecha de finalización')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']
    def __str__(self):
        return 'Curso: '+self.name

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    curse = models.ForeignKey(Curse, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
