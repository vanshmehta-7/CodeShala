# Generated by Django 3.1.2 on 2020-10-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]