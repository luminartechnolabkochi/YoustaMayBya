from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import CreateView
from yousta.forms import RegistrationForm
from yousta.models import User
from django.urls import reverse_lazy
from django.contrib import messages

class SignUpView(CreateView):

    template_name="yousta/register.html"
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("signup")

    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)

    






