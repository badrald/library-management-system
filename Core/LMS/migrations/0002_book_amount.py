# Generated by Django 4.1.7 on 2023-06-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
