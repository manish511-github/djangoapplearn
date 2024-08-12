from django.contrib import admin
from .models import CustomUser,Course,Enrollment
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserModel(UserAdmin):
    list_display=['username','user_type']

class CourseField(admin.ModelAdmin):
    list_display = ['id','title']

class EnrollmentField (admin.ModelAdmin):
    list_display =['student','course']
   
admin.site.register(CustomUser,UserModel)
admin.site.register(Course,CourseField)
admin.site.register(Enrollment,EnrollmentField)