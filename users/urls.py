from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_view
from users import views


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_view.LoginView.as_view(
                                                     template_name='users/login.html',
                                                     redirect_field_name=''
                                              ), name='login'),
    path('logout/', auth_view.LogoutView.as_view(
                                                         template_name='users/logout.html',
                                                         redirect_field_name=''
                                                  ), name='logout'),

    path('profile/', profile, name='profile'),
    path('delete_user<int:pk>/',views.DeleteUser.as_view(),name='delete_user'),
    # path('user_detail<int:pk>/',views.User_Detail,name='user_detail')





]
