# Generated by Django 3.1.2 on 2020-10-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0003_auto_20201021_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]