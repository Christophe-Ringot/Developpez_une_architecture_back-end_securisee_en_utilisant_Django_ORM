# Generated by Django 4.0 on 2022-01-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0008_alter_contract_payment_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='payment_due',
            field=models.DateTimeField(),
        ),
    ]
