from rest_framework.urls import path
from . import views

urlpatterns = [
    path('studentc01/', views.get_studentc01, name='studentc01'),
    path('studentc01/<int:pk>/', views.get_studentco1_details, name='studentc01-details'),
    path('studentc01/create/', views.create_studentco1, name='create-studentc01'),
    path('studentc01/<int:pk>/update/', views.update_studentco1, name='update-studentc01'),
    path('studentc01/<int:pk>/delete/', views.delete_studentco1, name='delete-studentc01'),
]

