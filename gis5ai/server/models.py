from django.db import models
from django.urls import reverse

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
