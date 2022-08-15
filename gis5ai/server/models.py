from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, help_text='Enter your team name')

    def __str__(self):
        return self.name
