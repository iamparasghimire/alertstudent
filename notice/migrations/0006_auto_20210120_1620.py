# Generated by Django 3.1.5 on 2021-01-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_auto_20210120_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
