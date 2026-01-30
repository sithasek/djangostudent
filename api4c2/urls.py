from rest_framework.urls import path
from . import views
urlpatterns = [
    path('student4c2/', views.student4c2_list_create, name='student4c2-list-create'),
    path('student4c2/<int:pk>/', views.student4c2_detail, name='student4c2-detail'),
    path('login4c2/', views.login4c2, name='login4c2'),
]
