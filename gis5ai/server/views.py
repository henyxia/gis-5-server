from django.shortcuts import render
from django.views import generic

from .models import Team

def index(request):
    num_teams = Team.objects.all().count()

    context = {
        'num_teams': num_teams,
    }

    return render(request, 'index.html', context=context)

class TeamListView(generic.ListView):
    model = Team
    context_object_name = 'team_list'
    queryset = Team.objects.all()
