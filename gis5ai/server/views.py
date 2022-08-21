from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from datetime import datetime

from .models import Team, Challenge, ChallengeInstance, ChallengeAttempt
from challenge import *

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

def ChallStart(request, chall_id, team_id):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            inst = ChallengeInstance(challenge_id=chall_id, team_id=team_id)
            inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('chall-work', kwargs={'chall_id': chall_id, 'team_id': team_id}))

    else:
        chall = Challenge.objects.get(pk=chall_id)
        team = Team.objects.get(pk=team_id)
        context = {
            'chall': chall,
            'team': team,
        }
        return render(request, 'server/challengeinstance_form.html', context=context)

def ChallWork(request, chall_id, team_id):
    chall = Challenge.objects.get(pk=chall_id)
    team = Team.objects.get(pk=team_id)
    context = {
        'chall': chall,
        'team': team,
    }
    return render(request, 'server/challengeinstance_detail.html', context=context)

def ChallCheck(request, chall_id, team_id):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('chall-work', chall_id=chall_id, team_id=team_id))

    form = forms.Form(request.POST)
    if not form.is_valid():
        return HttpResponseRedirect(reverse('chall-work', chall_id=chall_id, team_id=team_id))

    # get chall validator function
    chall = Challenge.objects.get(pk=chall_id)
    validator_module = globals()[chall.validator]
    validator = getattr(validator_module, chall.validator)
    team = Team.objects.get(pk=team_id)
    attempt = validator(team.base_url)

    att = ChallengeAttempt(challenge_id=chall_id, team_id=team_id, correct=attempt.correct, details=attempt.result_entries)
    att.save()

    if att.correct:
        instances = ChallengeInstance.objects.filter(team_id=team_id, challenge_id=chall_id)
        inst = instances[0]
        inst.status = 'c'
        inst.done_at = datetime.now()
        inst.save()

    # redirect to a new URL:
    return HttpResponseRedirect(reverse(
        'chall-check-view', kwargs={
            'chall_id': chall_id,
            'team_id': team_id,
            'attempt_id': att.id,
        }
    ))

def ChallCheckView(request, chall_id, team_id, attempt_id):
    chall = Challenge.objects.get(pk=chall_id)
    team = Team.objects.get(pk=team_id)
    attempt = ChallengeAttempt.objects.get(pk=attempt_id)
    context = {
        'chall': chall,
        'team': team,
        'attempt': attempt,
    }

    return render(request, 'server/challengeinstance_check.html', context=context)

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
