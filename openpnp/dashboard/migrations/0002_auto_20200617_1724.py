# Generated by Django 3.0.6 on 2020-06-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='description',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='templateattribute',
            name='description',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='templateskill',
            name='description',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='templateattribute',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='templateskill',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
