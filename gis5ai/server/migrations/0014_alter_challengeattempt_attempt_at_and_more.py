# Generated by Django 4.1 on 2022-09-04 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_challenge_10'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengeattempt',
            name='attempt_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='challengeinstance',
            name='started_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
