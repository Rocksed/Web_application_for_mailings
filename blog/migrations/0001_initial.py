# Generated by Django 4.2.1 on 2023-06-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.CharField(verbose_name='содержимое статьи')),
                ('img', models.ImageField(upload_to='blog/', verbose_name='изображение')),
                ('views', models.IntegerField(verbose_name='кол-во просмотров')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='дата публикации')),
            ],
        ),
    ]
