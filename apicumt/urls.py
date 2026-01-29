from . import views
from rest_framework.urls import path

urlpatterns = [
    path('students/', views.get_students, name='get_students'),
    path('students/login/', views.login_student, name='login_student'),
    path('students/<int:pk>/', views.get_student_details, name='get_student_details'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/update/<int:pk>/', views.update_student, name='update_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
]

