# Generated by Django 4.0 on 2021-12-29 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_alter_contract_status'),
        ('customers', '0003_remove_customer_sales_contract'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('events', '0002_alter_events_contract'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
