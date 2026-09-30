from django.urls import path
from project.views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_project/', add_project, name='add_project'),
    path('project_list/', project_list, name='project_list'),
    path('update_project/<str:p_id>/', update_project, name='update_project'),
    path('delete_project/<str:p_id>/', delete_project, name='delete_project'),


    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
]