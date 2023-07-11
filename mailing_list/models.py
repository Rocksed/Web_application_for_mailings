from django.db import models

from users.models import User

NULLABLE = {'blank': True,
            'null': True}


class CLIENT(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='отчество', **NULLABLE)
    email = models.EmailField(verbose_name='почта')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class MESSAGE(models.Model):
    letter_subject = models.CharField(max_length=200, verbose_name='тема письма')
    letter_body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'{self.letter_subject}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class SETTINGS(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('CREATED', 'Создана'),
        ('LAUNCHED', 'Запущена'),
        ('COMPLETED', 'Завершена')

    ]

    start_time = models.DateField(verbose_name='начало рассылки', **NULLABLE)
    end_time = models.DateField(verbose_name='конец рассылки', **NULLABLE)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, **NULLABLE)
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='статус рассылки', max_length=50)
    clients = models.ManyToManyField(CLIENT, verbose_name='клиенты')
    message = models.ForeignKey(MESSAGE, verbose_name='сообщение', on_delete=models.CASCADE, **NULLABLE)
    last_run = models.DateField(verbose_name='дата последней отправки рассылки', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)

    def __str__(self):
        return f'{self.message} {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        permissions = [
            ('can_deactivate_settings',
             'Can deactivate settings')
        ]


class ATTEMPT(models.Model):
    settings = models.ForeignKey(SETTINGS, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
    message = models.CharField(verbose_name='сообщение')
    date = models.DateTimeField(verbose_name="дата и время попытки")
    status = models.BooleanField(verbose_name='статус попытки')
    server_answer = models.CharField(verbose_name='ответ сервера', **NULLABLE)

    def __str__(self):
        return f'{self.message} {self.date} {self.status}'

    class Meta:
        verbose_name = 'попытка'

        verbose_name_plural = 'попытки'


