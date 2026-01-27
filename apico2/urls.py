from rest_framework.urls import path
from . import views
urlpatterns = [
    path('studentc02/', views.get_studentc02, name='studentc02'),
    path('studentc02/<int:pk>/', views.get_studentco2_details, name='studentc02-details'),
    path('studentc02/create/', views.create_studentco2, name='create-studentc02'),
]