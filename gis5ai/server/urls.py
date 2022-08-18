from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('teams/', views.TeamListView.as_view(), name='teams'),
        path('teams/<int:pk>', views.TeamDetailView, name='team-detail'),
        path('teams/create/', views.TeamCreate.as_view(), name='team-create'),
        path('challs/', views.ChallListView.as_view(), name='challs'),
        path('challs/<int:pk>', views.ChallDetailView.as_view(), name='chall-detail'),
        path('challs/create/', views.ChallCreate.as_view(), name='chall-create'),
    ]
