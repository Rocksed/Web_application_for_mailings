from django.db import models

from mailing_list.models import NULLABLE


# Create your models here.
class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='содержимое статьи')
    img = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    views = models.IntegerField(verbose_name='кол-во просмотров', **NULLABLE)
    date = models.DateTimeField(auto_now=True, verbose_name='дата публикации', **NULLABLE)
