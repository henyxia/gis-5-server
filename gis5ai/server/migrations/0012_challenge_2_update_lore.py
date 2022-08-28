# Generated by Django 4.1 on 2022-08-28 12:47

from django.db import migrations

def challenge_2_update(apps, schema_editor):
    Challenge = apps.get_model('server', 'Challenge')
    challs = Challenge.objects.filter(name='My name is Bond, API Bond')
    chall = challs[0]
    chall.description="""# Well played!
Your API is now alive and you reach the first step of many more to come!
As seen during the course, managing secrets is an important part.
Your API will have to use one on a specific endpoint.

On Vault, a secret has been setup for you.
This secret is the token your API will use later.
To access it, create a template for environmental variable in your Nomad file.
Create an environmental variable named `API_SECRET`.
In your template, use the secret from `gis_kv/team_XX/token`.

## Goal
You will create an endpoint named `/identify`.
This endpoint will expose a `hmac` result.
This result will be the digest of the `sha256` function with the key being the content of `API_SECRET` and the message a challenge.
This challenge will be given with a `POST` call on your endpoint, with the following data.
```
{
    "challenge": "a random challenge"
}
```
Your API will respond with the following data:
```
{
    "digest": "ba1ae768184d395ca1c9f79fb66584d2e2f71313c737c4dd6863f0602dea34df"
}
```
"""
    chall.save()

class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_challenge_2'),
    ]

    operations = [
        migrations.RunPython(challenge_2_update),
    ]
