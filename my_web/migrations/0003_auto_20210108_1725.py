# Generated by Django 3.1.4 on 2021-01-08 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_web', '0002_auto_20210103_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='time',
            new_name='time_field',
        ),
    ]