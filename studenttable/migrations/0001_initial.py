# Generated by Django 3.1.5 on 2021-01-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=155, null=True)),
                ('faculty', models.CharField(blank=True, max_length=155, null=True)),
                ('address1', models.CharField(blank=True, max_length=80, null=True)),
                ('address2', models.CharField(blank=True, max_length=80, null=True)),
                ('batch', models.CharField(blank=True, max_length=85, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
