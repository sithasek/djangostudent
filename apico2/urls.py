from rest_framework.urls import path
from . import views
urlpatterns = [
    path('studentc02/', views.get_studentc02, name='studentc02'),
    path('studentc02/<int:pk>/', views.get_studentco2_details, name='studentc02-details'),
    path('studentc02/create/', views.create_studentco2, name='create-studentc02'),
    path('studentc02/update/<int:pk>/', views.update_studentco2, name='update-studentc02'),
    path('studentc02/delete/<int:pk>/', views.delete_studentco2, name='delete-studentc02'),
    path('studentc02/login/', views.login_studentco2, name='login-studentc02'),
]
