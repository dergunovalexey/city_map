from django.db import models
from area.choices import LevelDangerous


class MicroArea(models.Model):
    left_desc = 'левый нижний угол квадрата'
    right_desc = 'правый нижний угол'
    latitude = 'Широта'
    longitude = 'Долгота'

    latitude_left = models.FloatField(verbose_name=latitude,
                                      help_text=left_desc)
    longitude_left = models.FloatField(verbose_name=longitude,
                                       help_text=left_desc)
    latitude_right = models.FloatField(verbose_name=latitude,
                                       help_text=right_desc)
    longitude_right = models.FloatField(verbose_name=longitude,
                                        help_text=right_desc)
    level = models.PositiveSmallIntegerField(
        choices=LevelDangerous.CHOICES, default=LevelDangerous.NOT,
        verbose_name='Уровень опасности участка')

    class Meta:
        verbose_name = 'Участок города'
        verbose_name_plural = 'Участки города'

    def __str__(self):
        return 'Участок дороги № {}'.format(self.id)
