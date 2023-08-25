from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView
from .models import CustomUser
from django.urls import reverse_lazy,reverse
from .forms import UserLoginForm,CustomerRegistrationForm
# Create your views here.

class HomeView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context
    
class UserRegistrationView(FormView):
    template_name="login.html"
    
    form_class=CustomerRegistrationForm
    
    success_url=reverse_lazy('mainapp:home')

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["type"]="signup"
        return context

class UserLoginView(FormView):
    form_class=UserLoginForm
    template_name="login.html"
    success_url=reverse_lazy('mainapp:home')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["type"]="login"
        return context



