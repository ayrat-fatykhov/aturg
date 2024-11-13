from django.db import models

class Log(models.Model):
    """
    Определяет поля для класса Лог
    """
    name = models.CharField(max_length=255, verbose_name='наименование')
    date = models.TextField(verbose_name='данные из лога')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Лог
        """
        return f'{self.name} - {self.date}'

    class Meta:
        """
        Определяет отображение модели Лог в админке. Сортирует по порядковому номеру
        """
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('pk',)
