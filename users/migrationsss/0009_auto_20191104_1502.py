# Generated by Django 2.2.6 on 2019-11-04 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191104_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='class_div',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='rollno',
        ),
    ]
