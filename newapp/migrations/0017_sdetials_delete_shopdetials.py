# Generated by Django 5.0.1 on 2024-03-16 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0016_remove_shopdetials_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='sdetials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('materialType', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('qty', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.pcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='shopdetials',
        ),
    ]
