# Generated by Django 4.1 on 2022-08-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='member1',
            field=models.CharField(default='login8', help_text='login8 of the first member', max_length=8),
        ),
        migrations.AddField(
            model_name='team',
            name='member2',
            field=models.CharField(blank=True, help_text='login8 of the second member', max_length=8),
        ),
        migrations.AddField(
            model_name='team',
            name='member3',
            field=models.CharField(blank=True, help_text='login8 of the third member', max_length=8),
        ),
    ]