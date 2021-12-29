# Generated by Django 4.0 on 2021-12-21 11:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('customers', '0001_initial'),
        ('contracts', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.TextField(choices=[('on_going', 'On going'), ('finished', 'Finished')])),
                ('attendees', models.IntegerField(default=0)),
                ('event_date', models.DateField(default=django.utils.timezone.now)),
                ('notes', models.TextField(blank=True, max_length=2500)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='customers.customers')),
                ('contract', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.contracts')),
                ('support_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
