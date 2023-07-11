from django.contrib import admin

from mailing_list.models import CLIENT, MESSAGE, SETTINGS, ATTEMPT
from users.models import User


# Register your models here.
@admin.register(CLIENT)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


@admin.register(MESSAGE)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('letter_subject',)


@admin.register(SETTINGS)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('message', 'status',)


@admin.register(ATTEMPT)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('message', 'date', 'status')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name']
