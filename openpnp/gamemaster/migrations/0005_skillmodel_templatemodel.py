# Generated by Django 3.0.6 on 2020-07-14 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gamemaster', '0004_auto_20200714_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('min_value', models.IntegerField(default=0)),
                ('max_value', models.IntegerField(default=100)),
                ('related_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamemaster.TemplateModel')),
            ],
        ),
    ]
