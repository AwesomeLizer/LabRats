from django.db import models


class Lab(models.Model):
    title = models.CharField('Название', max_length = 60)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'


class Expert(models.Model):
    fio = models.CharField('ФИО', max_length = 60)
    department = models.CharField('Департамент', max_length = 60)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Экспериментатор'
        verbose_name_plural = 'Экспериментаторы'