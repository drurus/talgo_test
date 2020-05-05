from django.db import models
from json import dumps


class Activity(models.Model):
    """
    Список выбора деятельности
    """
    activity = models.CharField(max_length=100, help_text='Область деятельности', unique=True)

    def __str__(self):
        return self.activity


class User(models.Model):
    """
    Пользователь
    """
    login = models.CharField(max_length=75, primary_key=True, unique=True)
    name = models.CharField(max_length=25, help_text='Имя')
    lastname = models.CharField(max_length=50, help_text='Фамилия')
    age = models.SmallIntegerField(help_text='Возраст')
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT, help_text='Выбор деятельности', null=True)
    email = models.EmailField(help_text='e-mail', blank=True)
    social = models.CharField(max_length=100, help_text='Профиль Facebook/Instagram', blank=True, null=True)

    def __str__(self):
        return f'''{self.name} ({self.login})'''

    def display_activity(self):
        """
        Обрезать в админке длинные наименования
        """
        out = str(self.activity)
        mlen = 15
        if len(out) > mlen:
            out = '%s...' % out[:mlen]
        return out


class Shop(models.Model):
    """
    Товары
    """
    name = models.CharField(max_length=255, help_text='Наименование')
    descr = models.CharField(max_length=255, help_text='Описание', default='')
    code = models.CharField(max_length=10, help_text='Код товара', primary_key=True, unique=True)
    cost = models.IntegerField(help_text='Стоимость')

    def __str__(self):
        return str(dumps({'name': self.name, 'descr': self.descr, 'code': self.code, 'cost': self.cost}))
