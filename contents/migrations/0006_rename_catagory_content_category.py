# Generated by Django 3.2.6 on 2021-08-16 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_auto_20210816_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='catagory',
            new_name='category',
        ),
    ]