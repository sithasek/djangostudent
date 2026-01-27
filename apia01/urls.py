from rest_framework.urls import path
from . import views

urlpatterns = [
    path('studenta01/', views.get_studenta01, name='studenta01'),
    path('studenta01/<int:pk>/', views.get_studenta01_details, name='studenta01-details'),
    path('studenta01/create/', views.create_studenta01, name='create-studenta01'),
    path('studenta01/<int:pk>/update/', views.update_studenta01, name='update-studenta01'),
    path('studenta01/<int:pk>/delete/', views.delete_studenta01, name='delete-studenta01'),
]

