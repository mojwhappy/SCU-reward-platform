# Generated by Django 2.0.6 on 2019-12-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_platform', '0003_auto_20191125_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_class',
            field=models.CharField(choices=[('赏金模式', 'class_1'), ('猎人模式', 'class_2')], default='赏金模式', max_length=48),
        ),
    ]