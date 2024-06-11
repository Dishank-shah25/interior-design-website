# Generated by Django 5.0.1 on 2024-03-14 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0012_remove_product_category_delete_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bimage', models.ImageField(upload_to='photos', verbose_name='blog image')),
                ('title', models.CharField(max_length=30, verbose_name='blog title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.AlterField(
            model_name='gimage',
            name='image',
            field=models.ImageField(upload_to='photos', verbose_name='gallery image'),
        ),
        migrations.AlterField(
            model_name='gimage',
            name='title',
            field=models.CharField(max_length=30, verbose_name='title'),
        ),
    ]
