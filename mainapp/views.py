from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView

from django.urls import reverse_lazy,reverse

# Create your views here.

class HomeView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context
    
class RoomView(TemplateView):
    template_name="room.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        room_name=kwargs.get('room_name')
        context['room_name']=room_name
        return context


import random
def generate_pin(request):
    pin = str(random.randint(100000, 999999))
    
      
    return HttpResponse("Users please enter this secure pin to connect " + pin)