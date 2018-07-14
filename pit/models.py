from django.db import models


class Pit(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    number_of_jolting = models.PositiveIntegerField(
        verbose_name='Количество толчков')
    speed = models.FloatField(verbose_name='Скорость')
    created_at = models.DateTimeField(verbose_name='Дата и время создания',
                                      auto_now_add=True)

    class Meta:
        verbose_name = 'Сигнал неровности дороги'
        verbose_name_plural = 'Сигналы неровности дороги'

    def __str__(self):
        return 'Сигнал неровности дороги №{}'.format(self.id)
