"""
URL configuration for bank_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from users.views import MyProfileView, TransactionPageView, MakeTransactionView, LoginPageView, \
    UserRegistrationView, UserMakeRegistrationView, UserMakeLoginView, DepozitView, AddMoneyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-profile/', MyProfileView.as_view(), name='my-profile-url'),
    path('depozit/', DepozitView.as_view(), name='depozit-url'),
    path('add-money/', AddMoneyView.as_view(), name='add-money-url'),
    path('transaction/', TransactionPageView.as_view(), name='transaction-url'),
    path('make-transaction/', MakeTransactionView.as_view(), name='make-transaction-url'),
    path('login-page/', LoginPageView.as_view(), name='user-login'),
    path('user-make-login/', UserMakeLoginView.as_view(), name='user-make-login'),
    path('user-registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('user-make-registration/', UserMakeRegistrationView.as_view(), name='user-make-registration'),


]
