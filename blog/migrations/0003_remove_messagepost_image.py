# Generated by Django 3.0.6 on 2020-08-20 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_messagepost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagepost',
            name='image',
        ),
    ]