# Generated by Django 4.0 on 2021-12-22 12:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_alter_contracts_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField()),
                ('amount', models.FloatField()),
                ('payment_due', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='contracts',
            name='client',
        ),
        migrations.RemoveField(
            model_name='contracts',
            name='sales_contract',
        ),
    ]
