from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('teams/', views.TeamListView.as_view(), name='teams'),
        path('teams/<int:pk>', views.TeamDetailView.as_view(), name='team-detail'),
        path('teams/create/', views.TeamCreate.as_view(), name='team-create'),
    ]
