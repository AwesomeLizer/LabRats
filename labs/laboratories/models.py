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


class Sample(models.Model):
    name = models.CharField('Наименование', max_length = 50)
    code = models.CharField('Код образца', max_length = 10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Образец'
        verbose_name_plural = 'Образцы'


class Experiment(models.Model):
    lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE)
    sample_id = models.ForeignKey(Sample, on_delete=models.CASCADE)
    expert_id = models.ManyToManyField(Expert)

    def __str__(self):
        return self.lab_id.title + ' - ' + self.sample_id.name

    class Meta:
        verbose_name = 'Эксперимент'
        verbose_name_plural = 'Эксперименты'