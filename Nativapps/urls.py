"""Nativapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from school.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import static

#importamos lo del folder views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('curses/new', create_course, name='course_create'),
    path('curses/list', course_list, name='course_list'),
    path('curses/<int:id>', course_detail, name='course_detail'),
    path('curses/<int:id>/delete', course_delete, name='course_delete'),
    path('students/new', student_create, name='student_create'),
    path('students/list', student_list, name='student_list'),
    path('students/<int:id>', student_detail, name='student_detail'),
    path('students/<int:id>/delete', student_delete, name='student_delete'),
    path('students/top_3', student_top_3, name='student_top_3'),   
    path('', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', signout, name='logout'),
    path('dashboard/', dashboard, name='dashboard')
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)