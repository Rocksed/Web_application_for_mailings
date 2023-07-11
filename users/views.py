from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, TemplateView, CreateView, ListView, DeleteView

from users.forms import ProfileForm, UserRegisterForm
from users.models import User, EmailVerification
import uuid
from datetime import timedelta
from django.utils.timezone import now


# Create your views here.

class ProfileUpdateView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def EmailVerificated(request):
    """Контроллер вызывается, когда пользователь нажимает на кнопку подтвердить почту"""
    current_user = request.user
    expiration = now() + timedelta(hours=24)

    record = EmailVerification.objects.create(  # запись данных в бд

        code=uuid.uuid4(),
        user=current_user,
        expiration=expiration,

    )

    record.send_verification_email()  # отправка сообщения

    return render(request, 'users/email.html')


class EmailVerificationView(TemplateView):
    """Контроллер вызывается, когда пользователь переходит по ссылке из сообщения"""
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists():
            user.is_verified_email = True
            user.save()
            return super().get(self, request, *args, **kwargs)


class UserLogin(LoginView):
    model = User

    def form_valid(self, form):
        """Доп.проверка здесь сделана, для того чтобы менеджеры могли блокировать пользовоателя, но при этом он не удалялся из базы данных"""

        email = form.cleaned_data['username']
        obj = User.objects.get(email=email)
        if obj.is_active:  # если пользователь активен, то его пропускает

            return super().form_valid(form)
        else:  # если нет, то его перекидывает на страницу с сообщением где говорится что он заблокирован
            return render(self.request, 'users/block.html')


class RegisterView(CreateView):
    model = User

    template_name = 'users/register_form.html'

    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.view_user'


class UserDelete(DeleteView):
    model = User

    success_url = reverse_lazy('users:users')


def toggle_activity(request, pk):
    """Контроллер для блокировки пользователя"""
    obj = User.objects.get(pk=pk)

    if obj.is_active:
        obj.is_active = False
        obj.save()

    else:
        obj.is_active = True
        obj.save()

    return redirect(reverse('users:users'))
