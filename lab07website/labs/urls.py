# /lab07/lab07website/labs/urls.py

from django.urls import path
from . import views
from .models import Lab

app_name='labs'

urlpatterns = [
    path('', views.LabsListView.as_view(),name='lab_list'),
    path('<int:pk>/', views.LabsDetailView.as_view(),name='lab_detail'),
    ]

