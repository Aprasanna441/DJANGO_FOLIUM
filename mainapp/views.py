from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.views import APIView

from django.contrib import messages
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
    # user=User.objects.create_user("john")
      
    return HttpResponse("Users please enter this secure pin to connect " + pin)


from rest_framework.response import Response
from  rest_framework import status
from .serializers import LocationSerializer
from geopy.distance import geodesic
from django.http import JsonResponse


from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny

class LocationView(APIView):
    permission_classes = [AllowAny]
    
    @csrf_exempt
    def post(self,request,format=None):
        serializer=LocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("hi")
            latitude=serializer.data.get('latitude')
            longitude=serializer.data.get('longitude')
            latitude1=serializer.data.get('latitude1')
            longitude1=serializer.data.get('longitude1')
            location=float(latitude), float(longitude)
            location1=float(latitude1),float(longitude1)
           
    
            distance=geodesic(location,location1).kilometers
            response_data = {'distance': distance}
            return JsonResponse(response_data,status=200,safe=False)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST,safe=False)

    
    

   
    
