from django.db import models
from datetime import datetime
import string, random


def random_string():
    s = string.ascii_letters + string.digits + '-_'
    x = "".join([random.choice(s) for i in range(random.randrange(10, 20))])
    return x


class Info(models.Model):
    i_title = models.TextField('Заголовок')
    i_text = models.TextField('Текст')
    i_time = models.DateTimeField('Время публикации', default=datetime.now)

    def __str__(self):
        return self.i_title

    class Meta:
        verbose_name = 'Рекламная запись'
        verbose_name_plural = 'Рекламные записи'


class AWARE_Page(models.Model):
    title = models.CharField('Название страницы', max_length=255, default='Не удалось получить заголовок страницы')
    page_html_code = models.TextField('HTML код страницы', default='<p>Ошибка парсинга страницы...</p>')
    unique_id = models.CharField('Уникальный ID', max_length=255, unique=True, default=random_string)
    time = models.DateTimeField('Время создания', default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/aware/%s/" % self.unique_id

    class Meta:
        verbose_name = 'Страница AWARE'
        verbose_name_plural = 'Страницы AWARE'


class Statistic(models.Model):
    u_stat = models.IntegerField('Стастика пользователей')
    b_stat = models.IntegerField('Статистика бота')
    st_time = models.DateTimeField('Время обновления', default=datetime.now)

    def __str__(self):
        return str(int(self.u_stat) + int(self.b_stat))

    class Meta:
        verbose_name = 'Статистика бота'
        verbose_name_plural = 'Статистика бота'