from django.db import models


class Help_request(models.Model):
    HELP_TYPE=(
        ('can_help', 'Хочу помочь'),
        ('need_help', 'Нужна помощь')
    )
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    number = models.CharField(max_length=255, verbose_name='Номер телефона')
    help_type = models.CharField(max_length=20, choices=HELP_TYPE)
    city = models.CharField(max_length=100, verbose_name='Город/село')
    info = models.TextField(verbose_name='Описание')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ' Запрос '
        verbose_name_plural = 'Запросы'
        ordering = ['-date_pub']
