# Generated by Django 3.1.2 on 2020-10-22 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='attachment',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
