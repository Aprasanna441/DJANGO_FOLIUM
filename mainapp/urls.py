from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import HomeView,RoomView
from mainapp import views

app_name="mainapp"
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('<str:room_name>/',RoomView.as_view(),name="room"),
    path('/generate_pin',views.generate_pin,name="generate_pin")
    



]