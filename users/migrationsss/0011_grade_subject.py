# Generated by Django 2.2.6 on 2019-11-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20191104_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='Subject',
            field=models.CharField(default='Design Project', max_length=30),
        ),
    ]
