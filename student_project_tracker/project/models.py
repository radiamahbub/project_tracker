from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    student_id = models.PositiveIntegerField(null=True)
    student_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.username}'

class ProjectModel(models.Model):
    PROJECT_STATUS = [
        ('NotStarted','NotStarted'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
    ]
    project_name = models.CharField(max_length=200, null=True)
    project_description = models.TextField( null=True)
    project_image = models.ImageField(upload_to='media/project_img', null=True)
    project_status = models.CharField(choices=PROJECT_STATUS, max_length=20, null=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    deadline = models.DateField(null=True)  
    created_at= models.DateField(auto_now_add=True, null=True) 
    updated_at = models.DateField(auto_now=True, null=True) 

    def __str__(self):
            return f'{self.project_name}'


class CourseModel(models.Model):
     CATEGORY = [
          ('CSE','CSE'),
          ('EEE','EEE'),
          ('CIVIL','CIVIL'),
     ]
     course_name = models.CharField(max_length=200, null=True)
     description = models.TextField(null=True)
     category = models.CharField(choices=CATEGORY, max_length=20, null=True)
     course_image = models.ImageField(upload_to='media/course_img', null=True)
     course_fee = models.IntegerField(null=True)

     def __str__(self):
          return f'{self.course_name}'