# Generated by Django 4.0.6 on 2022-08-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_alter_main_page_slider_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('promo_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='product_images')),
                ('information', models.TextField(max_length=1000)),
                ('subcategory_id', models.PositiveIntegerField()),
                ('add_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('add_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='main_page_slider',
            name='image',
            field=models.ImageField(upload_to='main_page_slider'),
        ),
    ]
