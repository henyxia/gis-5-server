from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView

from .models import Team, Challenge

def index(request):
    num_teams = Team.objects.all().count()
    num_challs = Challenge.objects.all().count()

    context = {
        'num_teams': num_teams,
        'num_challs': num_challs,
    }

    return render(request, 'index.html', context=context)

def TeamDetailView(request, pk):
    model = Team

    team = Team.objects.get(pk=pk)
    challs = team.get_challenges()

    context = {
        'team': team,
        'challs': challs,
    }

    return render(request, 'server/team_detail.html', context=context)

class TeamListView(generic.ListView):
    model = Team
    context_object_name = 'team_list'
    queryset = Team.objects.all()

class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'member1', 'member2', 'member3']

class ChallListView(generic.ListView):
    model = Challenge

class ChallCreate(CreateView):
    model = Challenge
    fields = ['name', 'priority', 'validator', 'description']

class ChallDetailView(generic.DetailView):
    model = Challenge
