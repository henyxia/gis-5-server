from django.db import models
from django.urls import reverse

from datetime import datetime

class Team(models.Model):
    name = models.CharField(max_length=100, help_text='Enter your team name')
    member1 = models.CharField(max_length=8, help_text='login8 of the first member', default='login8')
    member2 = models.CharField(max_length=8, help_text='login8 of the second member', blank=True)
    member3 = models.CharField(max_length=8, help_text='login8 of the third member', blank=True)
    base_url = models.CharField(max_length=100, help_text='Base URL to check API against')

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

    def get_current_chall(self):
        challs = self.get_challenges()

        for chall, inst in challs.items():
            if inst and inst.status == 's':
                return chall

        return None

    def get_next_chall(self):
        challs = self.get_challenges()

        lowest_chall = None
        for chall, inst in challs.items():
            # if no instance, the challenge has not been started
            if not inst:
                if lowest_chall is None or lowest_chall.priority > chall.priority:
                    lowest_chall = chall
                continue

        if lowest_chall is None:
            return None

        return lowest_chall

class Challenge(models.Model):
    name = models.CharField(max_length=100, help_text='Challenge name')
    priority = models.PositiveIntegerField(help_text='Challenge priority')
    minimal_version = models.CharField(max_length=12, help_text='Minimal API version required')
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

    def __str__(self):
        return "Challenge %d of team %d" % (self.challenge.id, self.team.id)

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

class ChallengeAttempt(models.Model):
    challenge = models.ForeignKey('Challenge', on_delete=models.RESTRICT)
    team = models.ForeignKey('Team', on_delete=models.RESTRICT)
    attempt_at = models.DateTimeField(blank=True, default=datetime.now)
    correct = models.BooleanField()
    details = models.JSONField()

    def __str__(self):
        return "Challenge %d of team %d: %s" % (self.challenge.id, self.team.id, "Success" if self.correct else "Failed")
