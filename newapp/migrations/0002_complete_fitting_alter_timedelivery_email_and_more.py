# Generated by Django 5.0.1 on 2024-02-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='complete_fitting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='user email')),
                ('message', models.TextField(verbose_name='user message')),
            ],
        ),
        migrations.AlterField(
            model_name='timedelivery',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='user email'),
        ),
        migrations.AlterField(
            model_name='timedelivery',
            name='message',
            field=models.TextField(verbose_name='user message'),
        ),
    ]