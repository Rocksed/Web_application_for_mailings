# Generated by Django 4.2.1 on 2023-07-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение'),
        ),
    ]