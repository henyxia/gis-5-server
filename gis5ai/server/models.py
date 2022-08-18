from django.db import models
from django.urls import reverse

from datetime import datetime

class Team(models.Model):
    name = models.CharField(max_length=100, help_text='Enter your team name')
    member1 = models.CharField(max_length=8, help_text='login8 of the first member', default='login8')
    member2 = models.CharField(max_length=8, help_text='login8 of the second member', blank=True)
    member3 = models.CharField(max_length=8, help_text='login8 of the third member', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team-detail', args=[str(self.id)])

    def get_members(self):
        members = [self.member1]
        if self.member2:
            members.append(self.member2)
            if self.member3:
                members.append(self.member3)

        return members

    def get_challenges(self):
        # get all challenges
        challenges = Challenge.objects.all()

        # get challenge instances
        started = True
        chall_instances = None
        try:
            chall_instances = ChallengeInstance.objects.filter(team=self.pk)
        except ChallengeInstance.DoesNotExist:
            started = False

        # prepare quick access map
        chall_insts = {}
        if started:
            for chall_instance in chall_instances:
                chall_insts[chall_instance.challenge.pk] = chall_instance

        # create final map
        challs = {}
        for challenge in challenges:
            if not started or not challenge.pk in chall_insts:
                challs[challenge] = None
                continue

            challs[challenge] = chall_insts[challenge.pk]

        return challs

class Challenge(models.Model):
    name = models.CharField(max_length=100, help_text='Challenge name')
    priority = models.PositiveIntegerField(help_text='Challenge priority')
    validator = models.CharField(max_length=100, help_text='Name of the validator function')
    description = models.TextField(help_text='Challenge description')

    ordering = ['priority']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chall-detail', args=[str(self.id)])

class ChallengeInstance(models.Model):
    challenge = models.ForeignKey('Challenge', on_delete=models.RESTRICT)
    team = models.ForeignKey('Team', on_delete=models.RESTRICT)
    started_at = models.DateTimeField(blank=True, default=datetime.now)
    done_at = models.DateTimeField(null=True, blank=True)

    CHALLENGE_STATUS = (
        ('s', 'Started'),
        ('c', 'Completed'),
    )
    status = models.CharField(
        max_length=1,
        choices=CHALLENGE_STATUS,
        blank=True,
        default='s',
        help_text='Challenge status',
    )
