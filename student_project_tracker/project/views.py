from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from project.models import *
from project.forms import *

# Create your views here.
@login_required
def home(request):
    return render(request, 'project/home.html')

def add_project(request):

    if request.method == "POST":
        project_name = request.POST.get('project_name')
        project_description = request.POST.get('project_description')
        project_image = request.FILES.get('project_image')
        project_status = request.POST.get('project_status')
        deadline = request.POST.get('deadline')

        ProjectModel.objects.create(
            project_name=project_name,
            project_description=project_description,
            project_image=project_image,
            project_status=project_status,
            created_by = request.user,
            deadline=deadline,
        )
        return redirect('project_list')

    return render(request, 'project/add_project.html')

def project_list(request):

    #p_data = ProjectModel.objects.all()
    p_data = ProjectModel.objects.filter(created_by=request.user)

    context = {
        'p_data':p_data
    }

    return render(request, 'project/project_list.html', context)

def update_project(request, p_id):
    p_data = ProjectModel.objects.get(id=p_id)

    if request.method == "POST":
            project_name = request.POST.get('project_name')
            project_description = request.POST.get('project_description')
            project_image = request.FILES.get('project_image')
            project_status = request.POST.get('project_status')
            deadline = request.POST.get('deadline')

            p_data.project_name =project_name
            p_data.project_description  =project_description

            if project_image:
                p_data.project_image =project_image

            p_data.project_status=project_status
            p_data.deadline =deadline

            p_data.save()

            return redirect('project_list')

    context = {
        'p_data':p_data
    }

    
    return render(request, 'project/update_project.html', context)

def delete_project(request, p_id):

    ProjectModel.objects.get(id = p_id).delete()

    return redirect('project_list')



def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_exist = UserModel.objects.filter(username=username).exists()

        if user_exist:
            messages.warning(request,'User already exists.')
            return redirect('register')

        if password == confirm_password:
            UserModel.objects.create_user(
                        username=username,
                        email=email, 
                        student_name=student_name,
                        student_id=student_id,
                        password=password,
                    )
            return redirect('login')

    return render(request, 'project/register.html')


def login_page(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_info = authenticate(request, username=username, password=password)

            if user_info:
                 login(request, user_info)
                 return redirect('home')
            else:
                 messages.warning(request,'Invalid Credentials.')
    return render(request, 'project/login.html')

def logout_page(request):

    logout(request)

    return redirect('login')


def add_course(request):
    form_data = CourseForm()
    if request.method == 'POST':
         form_data = CourseForm(request.POST, request.FILES)
         if form_data.is_valid():
              form_data.save()
              return redirect('course_list')

    context = {
         'form_data':form_data
    }
    return render(request, 'project/add_course.html', context)

def course_list(request):

     c_data = CourseModel.objects.all()

     context = {
          'c_data':c_data
     }
     return render(request, 'project/course_list.html', context)

def update_course(request, c_id):

     c_data = get_object_or_404(CourseModel, id=c_id)

     form_data = CourseForm(instance=c_data)

     if request.method == 'POST':
          form_data = CourseForm(request.POST, request.FILES, instance=c_data)
          if form_data.is_valid():
               form_data.save()
               return redirect('course_list')

          context = {
               'c_data':c_data
          }
     return render(request, 'project/update_course.html', context)

def delete_course(request, c_id):
     c_data = get_object_or_404(CourseModel, id=c_id)
     c_data.delete()
     return redirect('course_list')