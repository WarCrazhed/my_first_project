# Generated by Django 4.2.16 on 2024-10-22 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0003_car_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('publication_date', models.DateField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_first_app.publisher')),
            ],
        ),
    ]
