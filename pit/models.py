from django.db import models
from area.models import MicroArea
from area.choices import LevelDangerous


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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        obj, created = MicroArea.objects.get_or_create(
            latitude_left=self.latitude, longitude_left=self.longitude,
            latitude_right=self.latitude, longitude_right=self.longitude)
        if self.speed < 200:
            status = LevelDangerous.NOT
        elif self.speed < 600:
            status = LevelDangerous.LOW
        elif self.speed < 3000:
            status = LevelDangerous.MIDDLE
        else:
            status = LevelDangerous.HIGH
        obj.level = status
        obj.save()
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)
