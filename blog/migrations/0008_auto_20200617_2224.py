# Generated by Django 2.2.13 on 2020-06-17 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200617_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cventry',
            name='end_date',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cventry',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cventry',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='cventry',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]