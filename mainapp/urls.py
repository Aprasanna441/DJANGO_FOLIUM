from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import HomeView,RoomView

app_name="mainapp"
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('<str:room_name>/',RoomView.as_view(),name="room"),
    



]