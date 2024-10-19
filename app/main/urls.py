# app/main/urls.py

# Django modules
from django.urls import path

# My modules
from app.main import views

# Appname
app_name = 'main'

# Urlspatterns
urlpatterns = [
    # http://127.0.0.1:8000/blog/
    path('blog/', views.home_view, name='home'),
    # http://127.0.0.1:8000/blog/about/
    path('blog/about/', views.about_view, name='about'),
]

