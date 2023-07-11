from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from blog.models import Blog
from mailing_list.forms import ClientForm, SettingsForm, MessageForm
from mailing_list.models import CLIENT, MESSAGE, SETTINGS, ATTEMPT
from mailing_list.services import send_order_email, time_task


# Create your views here.

class MainView(TemplateView):
    """Контроллер отвечающий за отображение главной страницы"""
    template_name = 'mailing_list/main.html'

    def get_context_data(self, **kwargs):
        blog = Blog.objects.order_by('?')[:3]  # выборка из базы данных 3 случайных записи Blog
        clients_count = len(CLIENT.objects.all())  # подсчёт кол-во клиентов
        settings_count = len(SETTINGS.objects.all())  # подсчёт кол-во рассылок
        settings_active = len(SETTINGS.objects.filter(status='LAUNCHED'))  # подсчёт кол-во активных рассылок
        context = super().get_context_data()
        context['settings_count'] = settings_count
        context['settings_active'] = settings_active
        context['clients_count'] = clients_count
        context['blogs'] = blog

        return context


class ClientList(ListView):
    model = CLIENT


class ClientDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CLIENT

    def test_func(self):
        obj = self.get_object()

        return self.request.user == obj.author or self.request.user.is_superuser


class ClientCreate(LoginRequiredMixin, CreateView):
    model = CLIENT
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list:client_list')

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user  # запись в таблицу Client автора записи
        return super().form_valid(form)


class MailList(ListView):
    model = SETTINGS


class MessageDetail(DetailView):
    model = MESSAGE


class MailCreate(CreateView):
    model = SETTINGS
    form_class = SettingsForm

    success_url = reverse_lazy('mailing_list:mail_list')

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user  # запись в таблицу Settings автора записи

        time_task()  # как только создаётся новая рассылка, происходит вызов функции time_task()

        return super().form_valid(form)


class MailUpdate(UserPassesTestMixin, UpdateView):
    model = SETTINGS
    form_class = SettingsForm
    success_url = reverse_lazy('mailing_list:client_list')

    # form_class = ClientForm
    #
    def test_func(self):
        """Проверка является ли текущий пользователь автором рассылки или находится в группе managers"""
        obj = self.get_object()
        return self.request.user == obj.author or self.request.user.groups.filter(name='managers').exists()


class MailDetail(DetailView):
    model = SETTINGS


class MessageCreate(CreateView):
    model = MESSAGE

    form_class = MessageForm
    template_name = 'mailing_list/message_form.html'
    success_url = reverse_lazy('mailing_list:mail_list')

    def form_valid(self, form):
        return super().form_valid(form)


@permission_required('mailing_list.can_deactivate_settings')
def toggle_status(request, pk):
    """Контролер для отключения рассылкой"""

    obj = SETTINGS.objects.get(pk=pk)

    if obj.status == 'CREATED' or 'LAUNCHED':
        obj.status = 'COMPLETED'
        obj.save()

    return redirect(reverse('mailing_list:mail_list'))


class AttemptListView(ListView):
    model = ATTEMPT
