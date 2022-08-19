from django.contrib import admin

from .models import Team, Challenge, ChallengeInstance, ChallengeAttempt

admin.site.register(Team)
admin.site.register(Challenge)
admin.site.register(ChallengeInstance)
admin.site.register(ChallengeAttempt)
