# Generated by Django 2.0.13 on 2019-07-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionist', '0009_auto_20190705_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
