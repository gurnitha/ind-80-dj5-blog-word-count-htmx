# app/main/urls.py

# Django modules
from django.urls import path

# My modules
from app.main import views

# Appname
app_name = 'main'

# Urlspatterns
urlpatterns = [
    path('', views.home_view, name='home'),
]

