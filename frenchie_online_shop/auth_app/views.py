from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView

from frenchie_online_shop.auth_app.forms import RegisterForm


class UserRegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'