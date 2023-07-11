from django.contrib import admin

from users.models import EmailVerification


# Register your models here.
@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'created']
