# Generated by Django 4.0 on 2022-01-30 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
        ('events', '0003_remove_event_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='support_contact',
        ),
        migrations.AddField(
            model_name='event',
            name='contract',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.contract'),
        ),
    ]
