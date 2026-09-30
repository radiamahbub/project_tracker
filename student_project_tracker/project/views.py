from django.shortcuts import render, redirect
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from project.models import *

# Create your views here.
def home(request):
    return render(request, 'project/home.html')

def add_project(request):

    if request.method == "POST":
        project_name = request.POST.get('project_name')
        project_description = request.POST.get('project_description')
        project_image = request.FILES.get('project_image')
        project_status = request.POST.get('project_name')
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
            project_status = request.POST.get('project_name')
            deadline = request.POST.get('deadline')

            p_data.project_name =project_name,
            p_data.project_description  =project_description ,

            if project_image:
                p_data.project_image =project_image,

            p_data.project_status=project_status,
            p_data.deadline =deadline,

            p_data.save()

            return redirect('project_list')

    context = {
        'p_data':p_data
    }

    
    return render(request, 'project/update_project.html')

def delete_project(request, p_id):

    ProjectModel.objects.get(id = p_id).delete()

    return redirect('product_list')



def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')




    return render(request, 'project/register.html')

def login_page(request):

    return render(request, 'project/login.html')

def logout_page(request):

    return redirect('project/login')

