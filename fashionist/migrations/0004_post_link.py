# Generated by Django 2.0.13 on 2019-06-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionist', '0003_auto_20190608_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='', max_length=500),
        ),
    ]
