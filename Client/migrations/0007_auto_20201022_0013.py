# Generated by Django 3.1.2 on 2020-10-21 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0006_organization_desig_set'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='desig_set',
            new_name='desigset',
        ),
    ]
