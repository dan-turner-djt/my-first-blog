# Generated by Django 2.2.13 on 2020-06-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200617_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cventry',
            name='start_date',
            field=models.CharField(default='', max_length=200),
        ),
    ]