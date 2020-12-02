# Generated by Django 2.2.17 on 2020-12-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0011_add_default_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='remoterepository',
            name='remote_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='remoterepository',
            name='vcs_provider',
            field=models.CharField(blank=True, choices=[('GitHub', 'GitHub'), ('GitLab', 'GitLab'), ('Bitbucket', 'Bitbucket')], max_length=32, null=True, verbose_name='VCS provider'),
        ),
    ]
