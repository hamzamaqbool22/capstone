# Generated by Django 4.2.2 on 2023-09-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fittrack', '0007_calcount_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcount',
            name='goal',
            field=models.CharField(choices=[('Maintain Weight', 'Maintain Weight'), ('Weight Gain', 'Weight Gain'), ('Weight Loss', 'Weight Loss')], default=1, max_length=15),
        ),
    ]
