from django.shortcuts import render, HttpResponse,redirect
from .forms import SignUpForm,CourseForm
from .models import Course,Enrollment
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)

def base(request):
    user =request.user.is_authenticated
    print(user)
    return render(request,'learn/base.html',{'value':request.user})

    

# Create your views here.
def dologin(request):
    if not request.user.is_authenticated:
     fm=AuthenticationForm()
     return render(request,'learn/login.html',{"form":fm})
    return redirect("/profile")

def loginfn(request):
    
    if request.method=="POST":
        fm=AuthenticationForm(request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            print (uname)
            upass=fm.cleaned_data['password']
            print (upass)
            user = authenticate(username=uname, password=upass)
            if user is not None :
                login(request,user)
                messages.success(request,'Logged in Sucessfully')
                return redirect("/profile")
            
        else:
          
            messages.error(request,"Login Failed. Please Check the Credentials or Create new Account")
            fm=AuthenticationForm()
            return render(request,'learn/login.html',{"form":fm})
        
    else:
        fm=AuthenticationForm()
        return redirect("/profile")
 

            


def signup(request):
    if not request.user.is_authenticated:
      fm=SignUpForm()
      return render (request,'learn/signup.html',{'form':fm})
    return redirect("/profile")


def signupfn(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            print("Sucess")
            messages.success(request,'Account Created Sucessfully')    
            return redirect("/login")
        else:
             
            
             messages.error(request,fm.errors)
             print("Not Sucess")   
             fm=SignUpForm()
            #  fm=SignUpForm() 
            #  return render (request,'learn/signup.html',{'form':fm})
             return redirect('../signup')
    else:
        fm = SignUpForm()
        return redirect('../signup')
    
def profile(request):
    print(request.user)
    if request.user.is_authenticated:
        print("Authenticated")
        if request.user.user_type==3:
            return redirect("/student_board")
        elif request.user.user_type==2:
            return redirect("/teacher_board")
        elif request.user.user_type==1:
            return redirect("/admin_board")
    
    return  redirect(request,'/login')
        
def dologout(request):
    logout(request)
    print("Logout Sucessfully")
    messages.success(request,"Logout Sucessfully")
    return redirect("/login")            
            
# Teacher views

def teacher_dashboard(request):
    
    if request.user.is_authenticated and request.user.user_type==2:
        courses = Course.objects.filter(teacher=request.user)
        context = {
            'courses': courses
        }
        return render(request,'learn/teacher.html',context)
    messages.error(request,"Teacher not login.. login first")
    return redirect('/login')
# Create Course View
@login_required
def add_course(request):
    if request.method=="POST":
     fm=CourseForm(request.POST)
     if fm.is_valid():
         course=fm.save(commit=False)
         course.teacher=request.user
         course.save()
         messages.success(request,"Course Added Sucessfully")
         return redirect('/teacher_board')
     else:
         fm=CourseForm()
         messages.error(request,"Course Not Added")
         return redirect('/teacher_board')
    fm=CourseForm()
    return render(request, 'learn/createcourse.html', {'form': fm})

@login_required
def delete_course(request,courseid):
        try:
          course=Course.objects.get(id=courseid)
          course.delete()
          messages.success(request,"Course Deleted Sucessfully")
          return redirect('/teacher_board')
        except Course.DoesNotExist:
            return HttpResponse("Course not found.", status=404)
        
@login_required
def update_course(request,courseid):
    try :
        course=Course.objects.get(id=courseid)
    except Course.DoesNotExist:
        return HttpResponse("Course not found.", status=404)
    if request.method=="POST":
        fm=CourseForm(request.POST,instance=course)
        if fm.is_valid():
            fm.save()
            return redirect('/teacher_board')
    else :
        form=CourseForm(instance=course)

    return render(request, 'learn/createcourse.html', {'form': form, 'course': course})

def student_dashboard(request):
    if request.user.is_authenticated and request.user.user_type==3:
        all_courses = Course.objects.all()

        enrolled_courses = Enrollment.objects.filter(student=request.user).values_list('id', flat=True) 
        print(enrolled_courses)
        logger.warning("Already Sucessfully")
        
        available_courses = all_courses.exclude(id__in=enrolled_courses)

        context = {
            'enrolled_courses': Course.objects.filter(id__in=enrolled_courses),
            'available_courses': available_courses,
        } 
        return render(request,'learn/student.html',context) 
    messages.error(request,"Student not login.. login first")
    return redirect('/login')

def enroll_course(request,course_id):
    try:
        course=Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        messages.error(request,'Course not Found')
        return redirect('/student_board')
    
    existing_enrollement=Enrollment.objects.filter(student=request.user,course=course).first()
    if existing_enrollement:
        logger.info("Already Sucessfully")
        messages.info(request,f'You are already enrolled in {course.title}')
    else:
        Enrollment.objects.create(student=request.user,course=course)
        logger.info("Enroilled Sucessfully")
        messages.success(request, f'You have successfully enrolled in {course.title}.')

    return redirect('/student_board')

def disenroll_course(request,course_id):
    try:
        course=Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        messages.error(request,'Course Not Found')
        logger.info("Course not found")

        return redirect('/student_board')
    
    enrollment=Enrollment.objects.filter(student=request.user,course=course).first()
    if enrollment:
        enrollment.delete()
        messages.success(request, f'You have been successfully disenrolled from {course.title}.')
        logger.info("Sucess")

    else:
        messages.info(request, f'You are not enrolled in {course.title}.')
        logger.info("not enrolled in course")


    return redirect('/student_board')

def admin_board(request):
    if request.user.is_authenticated and request.user.user_type==1:
        return render(request,'learn/admin.html')
    messages.error(request,"Admin not login.. login first")
    return redirect('/login')
