import random
from django.db import models
from django.urls import reverse


class Card(models.Model):
    STATUS_CHOICES = (
        ('not_active', 'Не активирована'),
        ('active', 'Активирована'),
        ('overdue', 'Просрочена')
    )

    series = models.CharField(max_length=4, verbose_name='Серия')
    number = models.CharField(max_length=12, verbose_name='Номер')
    release_date = models.DateField(verbose_name='Дата выпуска')
    end_date = models.DateField(verbose_name='Дата окончания активности')
    use_date = models.DateField(verbose_name='Дата использования', null=True, blank=True)
    card_amount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма', default=0.0)
    status = models.CharField(max_length=15, verbose_name='Статус', choices=STATUS_CHOICES, default='not_active')

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
        ordering = ('release_date',)
        unique_together = ('series', 'number')

    def __str__(self):
        return '{0}{1}'.format(self.series, self.number)
    
    def get_absolute_url(self):
        return reverse('card', args=[self.id])

    @staticmethod
    def generate_string(size):
        return ''.join(random.choice('0123456789') for _ in range(size))
