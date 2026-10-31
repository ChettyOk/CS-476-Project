from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.filter_courses, name='search'),
]