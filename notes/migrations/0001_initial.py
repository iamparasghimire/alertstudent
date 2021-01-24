# Generated by Django 3.1.5 on 2021-01-23 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=155)),
                ('docfile', models.FileField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('fac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.faculty')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.semester')),
            ],
        ),
    ]
