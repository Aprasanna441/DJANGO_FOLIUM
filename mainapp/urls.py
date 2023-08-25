from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import HomeView,UserLoginView,UserRegistrationView

app_name="mainapp"
urlpatterns = [
    
    path('',HomeView.as_view(),name="home"),
    path('signup/',UserRegistrationView.as_view(),name="signup"),
    path('login/',UserLoginView.as_view(),name="login"),

]