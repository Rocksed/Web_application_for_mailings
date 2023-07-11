from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, **NULLABLE)
    email = models.EmailField(verbose_name='почта', unique=True)
    is_verified_email = models.BooleanField(default=False)
    is_active = models.BooleanField(verbose_name='активность', default=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class EmailVerification(models.Model):
    """Контроллер для работы с верификацией почты"""
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def send_verification_email(self):
        """Метод формирует ссылку на сайт и отправляет её по почте"""
        link = reverse('users:email_verify', kwargs={'email': self.user.email, 'code': self.code})
        verify_link = f'{settings.DOMAIN_NAME}{link}'

        send_mail(
            "Subject here",
            verify_link,
            settings.EMAIL_HOST_USER,
            [self.user.email],
            fail_silently=False,
        )
