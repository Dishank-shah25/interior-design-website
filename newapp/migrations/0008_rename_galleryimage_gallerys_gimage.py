# Generated by Django 5.0.1 on 2024-03-08 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_rename_gallery_gallerys'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallerys',
            old_name='galleryimage',
            new_name='gimage',
        ),
    ]
