from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_view.LoginView.as_view(
                                                     template_name='users/login.html',
                                                     redirect_field_name=''
                                              ), name='login'),
    path('logout/', auth_view.LogoutView.as_view(
                                                         template_name='blog/home.html',
                                                         redirect_field_name=''
                                                  ), name='logout'),
    path('profile/', profile, name='profile'),


]
