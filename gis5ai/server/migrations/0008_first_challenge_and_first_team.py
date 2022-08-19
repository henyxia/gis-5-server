# Generated by Django 4.1 on 2022-08-19 08:07

from django.db import migrations

def first_challenge(apps, schema_editor):
    Challenge = apps.get_model('server', 'Challenge')
    chall = Challenge(
        name="Hello API World",
        priority=1,
        minimal_version="0.0.1",
        validator="check_api_health",
        description="""# Welcome!
Hello, and welcome to this AI tutorial!

## Goal
The goal of this tutorial is to work on several AI algorithms and machine learning models.
And this, while keeping an "Ops" point-of-view.

For this first challenge, your goal will be to deploy your first API.
As seen during the course, you will have to use [Flask](https://flask.palletsprojects.com/en/2.2.x/).
Your API will only expose one endpoint, named `/version` and returning the following payload.
```
{
    "version": "0.0.1"
}
```

For the deployment part, you will reuse `.gitlab-ci.yml` and `project.nomad` from last year project.
Your image will be named `gis5ai/teamXX:VERSION` and your application will be named `teamXX`.
As for the `Dockerfile`, you can use the following one.
```
FROM python:3.10.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "/usr/local/bin/flask", "run", "--host=0.0.0.0" ]
```

The `requirements.txt` file will only contain the flask dependency in version `2.2.2`.
""",
    )
    chall.save()

def first_team(apps, schema_editor):
    Team = apps.get_model('server', 'Team')
    team = Team(
        name="Teachers",
        member1="jwasilewski",
        member2="rex",
    )
    team.save()

class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_challenge_minimal_version'),
    ]

    operations = [
        migrations.RunPython(first_challenge),
        migrations.RunPython(first_team),
    ]