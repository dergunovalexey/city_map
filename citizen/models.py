from django.db import models
from complaint.choices import ComplintStatus


class Citizen(models.Model):
    # user = models.ForeignKey('userdata.User', verbose_name='Пользователь')
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    address = models.CharField(max_length=256, verbose_name='Адрес')
    description = models.CharField(max_length=256, verbose_name='Описание')
    photo = models.ImageField(upload_to='complaints/', verbose_name='Фото',
                              default='default.JPG')
    latitude = models.FloatField(verbose_name='Широта', blank=True, null=True)
    longitude = models.FloatField(verbose_name="Долгота", blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        choices=ComplintStatus.CHOICES, default=ComplintStatus.PROCESSING,
        verbose_name='Статус')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата и время обновления')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return 'Заявка № {}'.format(self.id)
