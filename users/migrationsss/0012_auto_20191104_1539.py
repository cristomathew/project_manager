# Generated by Django 2.2.6 on 2019-11-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_grade_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='Subject',
            field=models.CharField(choices=[('Design Project', 'Design Project'), ('ASDL Lab', 'ASDL Lab')], default='Design Project', max_length=30),
        ),
    ]
