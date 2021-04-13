# Generated by Django 3.2 on 2021-04-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_web', '0019_auto_20210410_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aware_page',
            name='unique_id',
            field=models.CharField(default='9GEqEhEhrf5', max_length=255, unique=True, verbose_name='Уникальный ID'),
        ),
        migrations.AlterField(
            model_name='facts',
            name='unique_id',
            field=models.CharField(default='YPrS7OPbq1BG', max_length=32, unique=True, verbose_name='Уникальный ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='unique_id',
            field=models.CharField(default='PqB_2F8IVi', max_length=32, unique=True, verbose_name='Уникальный ID'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='unique_id',
            field=models.CharField(default='ypBJ6x8tMj5pPD', max_length=32, unique=True, verbose_name='Уникальный ID'),
        ),
    ]