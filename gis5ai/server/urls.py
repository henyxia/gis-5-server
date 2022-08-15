from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('teams/', views.TeamListView.as_view(), name='teams'),
    ]
