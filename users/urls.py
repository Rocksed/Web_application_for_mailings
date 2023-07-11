from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileUpdateView, EmailVerificated, EmailVerificationView, RegisterView, UserListView, \
    UserDelete, UserLogin, toggle_activity

app_name = UsersConfig.name
urlpatterns = [

    path('', UserLogin.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/email',  EmailVerificated, name='verify'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verify'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/toggle/<int:pk>/', toggle_activity, name='toggle')


]
