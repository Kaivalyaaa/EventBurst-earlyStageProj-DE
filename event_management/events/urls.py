# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # Add more URL patterns for other views as needed
    path('user_login/', views.user_login, name='user_login'),#--------for user-admin
    path('admin_login/', views.admin_login, name='admin_login'),#--------for user-admin
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),#--------for user-admin
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),#--------for user-admin
    path('set_user_credentials/', views.set_user_credentials, name='set_user_credentials'),#--------for user-admin
    path('logout/', views.logout, name='logout'),#--------for user-admin
]
