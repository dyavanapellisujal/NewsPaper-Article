from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.core.mail import send_mail


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Create your views here.
