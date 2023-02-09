from django.contrib import admin
from .models import Student, Curse, Registration


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    verbose_name = 'Estudiante'
    verbose_name_plural = 'Estudiantes'
class CurseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    verbose_name = 'Curso'
    verbose_name_plural = 'Cursos'
class RegistrationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    verbose_name = 'Inscripción'
    verbose_name_plural = 'Inscripciones'


admin.site.register(Student, StudentAdmin)
admin.site.register(Curse , CurseAdmin)
admin.site.register(Registration, RegistrationAdmin)
