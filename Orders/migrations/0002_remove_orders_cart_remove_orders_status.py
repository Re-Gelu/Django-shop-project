# Generated by Django 4.0.8 on 2022-10-21 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='status',
        ),
    ]
