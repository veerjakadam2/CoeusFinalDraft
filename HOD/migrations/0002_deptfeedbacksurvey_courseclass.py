# Generated by Django 3.1.4 on 2020-12-15 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deptfeedbacksurvey',
            name='courseclass',
            field=models.IntegerField(default=4, null=True),
        ),
    ]
