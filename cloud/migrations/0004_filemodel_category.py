# Generated by Django 2.2.10 on 2020-02-05 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0003_filemodel_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='category',
            field=models.CharField(default='normal', max_length=20),
        ),
    ]
