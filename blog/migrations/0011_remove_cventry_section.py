# Generated by Django 2.2.13 on 2020-06-18 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_cventry_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cventry',
            name='section',
        ),
    ]
