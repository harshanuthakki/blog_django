# Generated by Django 4.1.4 on 2023-01-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_desc',
            field=models.CharField(default='', max_length=250),
        ),
    ]
