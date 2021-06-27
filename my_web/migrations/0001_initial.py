# Generated by Django 3.2.2 on 2021-05-15 18:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import my_web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AWARE_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Не удалось получить заголовок страницы', max_length=255, verbose_name='Название страницы')),
                ('page_html_code', models.TextField(default='<p>Ошибка парсинга страницы...</p>', verbose_name='HTML код страницы')),
                ('unique_id', models.CharField(default=my_web.models.random_string, max_length=255, unique=True, verbose_name='Уникальный ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 5, 15, 18, 18, 28, 988968, tzinfo=utc), verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Страница AWARE',
                'verbose_name_plural': 'Страницы AWARE',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_text', models.TextField(verbose_name='Текст')),
                ('i_language', models.CharField(choices=[('ua', 'Украинский'), ('ru', 'Русский'), ('en', 'Английский')], default='ru', max_length=2, verbose_name='Язык')),
                ('i_active', models.CharField(choices=[('yes', 'Да'), ('no', 'Нет')], default='yes', max_length=3, verbose_name='Активно')),
                ('i_chance', models.IntegerField(max_length=3, verbose_name='Шанс отображения (от 1 до 100)')),
                ('i_views', models.PositiveIntegerField(default=0, editable=False, verbose_name='Просмотры')),
                ('i_time_active', models.DateTimeField(default=datetime.datetime(2021, 5, 15, 18, 18, 28, 918972, tzinfo=utc), verbose_name='Активно до')),
            ],
            options={
                'verbose_name': 'Рекламная запись',
                'verbose_name_plural': 'Рекламные записи',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_stat', models.IntegerField(verbose_name='Стастика пользователей')),
                ('b_stat', models.IntegerField(verbose_name='Статистика бота')),
                ('st_time', models.DateTimeField(default=datetime.datetime(2021, 5, 15, 18, 18, 28, 989972, tzinfo=utc), verbose_name='Время обновления')),
            ],
            options={
                'verbose_name': 'Статистика бота',
                'verbose_name_plural': 'Статистика бота',
            },
        ),
    ]