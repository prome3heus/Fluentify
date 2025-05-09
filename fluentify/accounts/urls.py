from django.urls import path
from . import views
from .views import DashboardView


app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]