# Generated by Django 4.2.2 on 2023-09-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fittrack', '0006_calcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcount',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=1, max_length=50),
        ),
    ]
