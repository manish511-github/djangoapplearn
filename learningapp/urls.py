"""
URL configuration for learningapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from learn import views as lv

urlpatterns = [
    path("", lv.base),
    path("admin/", admin.site.urls),
    path("login/",lv.dologin,name='dologin'),
    path("signup/",lv.signup,name='signup'),
    path("signuphelper/",lv.signupfn,name='signupfn'),
    path("loginfn/",lv.loginfn,name="loginfn"),
    path("profile/",lv.profile),
    path("logout/",lv.dologout,name="dologout"),
    path("teacher_board/",lv.teacher_dashboard),
    path("add_course/",lv.add_course,name="addcourse"),
    path('delete/<int:courseid>/', lv.delete_course, name='delete_course'),
    path('update/<int:courseid>/', lv.update_course, name='update_course'),
    path("student_board/",lv.student_dashboard),
    path("enroll_course/<int:course_id>/",lv.enroll_course,name='enroll_course'),
    path('disenroll/<int:course_id>/', lv.disenroll_course, name='disenroll_course'),
    path("admin_board/",lv.admin_board),
]
    
    
   

