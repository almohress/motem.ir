# Generated by Django 3.2.6 on 2021-08-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_content_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='multimedia',
            name='is_video',
            field=models.BooleanField(default=False),
        ),
    ]
