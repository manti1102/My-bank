from django.contrib.auth import login
from django.db import transaction
from django.http import request, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


# Create your views here.
class MyProfileView(TemplateView):
    template_name = 'profile-page.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user

        context = {
                'current_user': current_user
        }
        return context
class DepozitView(TemplateView):
    template_name = 'add-money-page.html'




class AddMoneyView(View):
    template_name ='add-money-page.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        user.balance += 10
        user.save()
        context = {
            'user': user
        }
        return render(request, self.template_name, context)
class TransactionPageView(TemplateView):
    template_name = 'transaction-page.html'

class MakeTransactionView(View):
    def post(self, request, *args,**kwargs):
        input_data = request.POST
        phone_number = input_data['phone_number']

        try:
            receiver = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            raise Http404
        sender = request.user
        if sender == receiver:
            return HttpResponse('Нельзя переводить в себе')

        with transaction.atomic():
            amount_value = input_data['amount']
            if int(amount_value) <= 0:
                return HttpResponse('нельзя переводить отрицательные значения')

            sender.balance -= int(amount_value)
            receiver.balance += int(amount_value)
            sender.save()
            receiver.save()

        return redirect('my-profile-url')

class UserRegistrationView(TemplateView):
    template_name = 'registration-page.html'



class LoginPageView(TemplateView):
    template_name = 'login-page.html'

class UserMakeLoginView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        phone_number = data['phone_number']
        password = data['password']


        user = CustomUser.objects.get(phone_number=phone_number)
        print('пользователь ', user)

        correct = user.check_password(password)
        print('коррект равен ', correct)

        if correct:
            login(request, user)

            return render(request,'profile-page.html', context={'current_user': user,
                                                                            'logged_in': True})
        else:
            return render(request, 'profile-page.html', context={'logged_in': False})





class UserMakeRegistrationView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST


        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:
            first_name = data['first_name']
            phone_number = data['phone_number']
            user = CustomUser.objects.create_user(
                password=password1, phone_number=phone_number,
                first_name=first_name,
            )
            login(request, user)

            context = {
                'current_user': user
            }
            return render(request, 'profile-page.html', context)
        else:
            pass

