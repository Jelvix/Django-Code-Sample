# Generated by Django 2.1.3 on 2019-01-23 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0002_tournamentpost_is_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(blank=True, null=True, verbose_name='start_date')),
                ('date_finish', models.DateTimeField(blank=True, null=True, verbose_name='finish_date')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='date_update')),
                ('matches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_tournament', to='cms.Tournament')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'events',
                'verbose_name': 'event',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_game', to='cms.Event'),
        ),
    ]
