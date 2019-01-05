"""confsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from confsite import settings
from home.views import Home
from sponsors.views import SponsorsList
from agenda.views import SpeakersList, Cfp
from accounts.views import MyAccount, Signup

urlpatterns = [
    path('admin/', admin.site.urls),
    # authentication
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html'),
         name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/change_password_done.html'),
         name='password_change_done'),
    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html',
                                              html_email_template_name='accounts/reset_password_email.html'),
         name='password_reset'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm.html'),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),
         name='password_reset_complete'),
    path('accounts/profile/',
         MyAccount.as_view(),
         name='user_account'),

    # regular site
    path('accounts/signup', Signup.as_view(), name='signup'),
    path('sponsors/', SponsorsList.as_view(), name='sponsors_list'),
    path('cfp/', Cfp.as_view(), name='cfp'),
    path('speakers/', SpeakersList.as_view(), name='speakers_list'),
    path('accounts/my_account/', MyAccount.as_view(), name='my_account'),
    path('', Home.as_view(), name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
