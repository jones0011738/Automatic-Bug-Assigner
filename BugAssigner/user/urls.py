from django.urls import path
from . import views
from django.contrib.auth import logout, views as auth_views

app_name = 'user'

urlpatterns = [
    #Post Views
    path('', views.user_register, name ='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_request, name='logout'),
    path('predictions/', views.predictions, name='predictions'),
    path('profile/', views.profile, name='profile'),
    path('password-reset', views.ChangePasswordView.as_view(), name='password_change')
]
