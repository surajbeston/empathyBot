"""empathy_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from api.views import test, get_id, create_questions, marks_db, get_data, analyse, get_students, get_students_notdone

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", test),
    path("id", get_id),
    path("fill_questions", create_questions),
    path("marks_db", marks_db),
    path("get_data", get_data),
    path("analyse/<ide>", analyse),
    path("get_students", get_students),
    path("get_students_notdone", get_students_notdone)
]
