from django.contrib import admin

from .models import Team, Challenge, ChallengeInstance

admin.site.register(Team)
admin.site.register(Challenge)
admin.site.register(ChallengeInstance)
