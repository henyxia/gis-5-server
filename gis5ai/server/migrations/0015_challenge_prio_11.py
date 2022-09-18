# Generated by Django 4.1 on 2022-09-10 16:03

from django.db import migrations

def challenge_4(apps, schema_editor):
    Challenge = apps.get_model('server', 'Challenge')
    chall = Challenge(
        name='Linear classification',
        priority=11,
        minimal_version="0.0.11",
        validator="algo_linear_class",
        description="""# Linear classification!
The KNN is done, well played!

Let's try the `RidgeClassifier` now.

Using the default settings and the same payload as before, create an endpoint on `/algo/linear/class`.

## Goal

You will have to return the predicted class with the precision associated.
```
{
  "predicted_class": 0,
  "precision": 0.8
}
```
""",
    )
    chall.save()


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_alter_challengeattempt_attempt_at_and_more'),
    ]

    operations = [
        migrations.RunPython(challenge_4)
    ]
