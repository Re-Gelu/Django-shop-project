# Generated by Django 4.0.6 on 2022-07-29 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_alter_main_page_slider_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_page_slider',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
