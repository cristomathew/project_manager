# Generated by Django 2.2.6 on 2019-11-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20191104_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='class_div',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='rollno',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
