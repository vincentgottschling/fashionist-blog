# Generated by Django 2.0.13 on 2019-06-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionist', '0004_post_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('age', models.CharField(default='', max_length=200)),
                ('hobbies', models.CharField(default='', max_length=200)),
                ('favourite_food', models.CharField(default='', max_length=200)),
                ('about_me', models.TextField(default='')),
            ],
        ),
    ]
