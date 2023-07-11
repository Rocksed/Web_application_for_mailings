from django.apps import AppConfig
from django.urls import path
from django.views.decorators.cache import cache_page

from mailing_list.apps import MailingListConfig
from mailing_list.views import ClientList, ClientDetail, MailList, MailDetail, MailCreate, ClientCreate, \
    MailUpdate, MessageDetail, MessageCreate, toggle_status, MainView, AttemptListView

app_name = MailingListConfig.name


urlpatterns = [
    path('',  cache_page(60)(MainView.as_view()), name='main'),
    path('clients/',  ClientList.as_view(), name='client_list'),
    path('add/', ClientCreate.as_view(), name='client_add'),
    path('detail/<int:pk>/', ClientDetail.as_view(), name='client_detail'),
    path('detail/toggle_status/<int:pk>/', toggle_status, name='toggle_status'),
    path('mailing_list/', MailList.as_view(), name='mail_list'),
    path('mailing_list/det/<int:pk>/', MessageDetail.as_view(), name='mail_detail'),
    path('mailing_list/update/<int:pk>/', MailUpdate.as_view(), name='mail_update'),
    path('mailing_list/detail/<int:pk>/', MailDetail.as_view(), name='mail_det'),
    path('mailing_list/create_mail/', MailCreate.as_view(), name='mail_create'),
    path('mailing_list/create_message/', MessageCreate.as_view(), name='message_create'),
    path('mailing_list/attempt/', AttemptListView.as_view(), name='attempts')




]