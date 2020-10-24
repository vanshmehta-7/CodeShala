# Generated by Django 3.1.2 on 2020-10-24 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('doj', models.DateTimeField(auto_now_add=True)),
                ('dob', models.DateTimeField()),
                ('age', models.IntegerField(null=True)),
                ('points', models.IntegerField()),
                ('designation', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Client.emp')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(max_length=500)),
                ('default_pts', models.IntegerField()),
                ('project_create_file', models.FileField(blank=True, null=True, upload_to='projectcreate/')),
                ('c_pts', models.IntegerField()),
                ('b_pts', models.IntegerField()),
                ('total', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('checksum', models.IntegerField(default=0)),
                ('available_points', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.parent')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('child', models.ManyToManyField(to='Client.Child')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.parent')),
            ],
        ),
        migrations.CreateModel(
            name='Voting_Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank1', models.IntegerField(default=0)),
                ('rank2', models.IntegerField(default=0)),
                ('rank3', models.IntegerField(default=0)),
                ('checksum', models.IntegerField(default=0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.emp')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.project')),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_pts', models.IntegerField()),
                ('emp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Client.emp')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Client.project')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Client.team')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_project', models.FileField(blank=True, null=True, upload_to='files/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('after_deadline', models.BooleanField(default=False)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.child')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.project')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.team')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.team'),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('confirmed', models.BooleanField(default=False)),
                ('desigset', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='emp',
            name='organization',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Client.organization'),
        ),
        migrations.AddField(
            model_name='emp',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.TextField()),
                ('priority', models.IntegerField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.organization')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='emp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Client.emp'),
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ManyToManyField(blank=True, to='Client.Parent'),
        ),
    ]
