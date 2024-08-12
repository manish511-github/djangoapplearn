from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser,Course

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 
    class Meta:
        model=CustomUser
        fields = ['username', 'first_name', 'last_name', 'email',"user_type"]
        labels = {'email': 'Email'} 
    
class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['title','description']