from django.shortcuts import render

from .models import Team

def index(request):
    num_teams = Team.objects.all().count()

    context = {
        'num_teams': num_teams,
    }

    return render(request, 'index.html', context=context)
