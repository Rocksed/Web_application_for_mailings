# Generated by Django 4.2.1 on 2023-07-11 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='views',
            field=models.IntegerField(blank=True, null=True, verbose_name='кол-во просмотров'),
        ),
    ]
