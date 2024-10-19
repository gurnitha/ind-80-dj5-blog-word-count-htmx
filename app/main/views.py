# app/main/views.py

# Django modules
from django.shortcuts import render


def home_view(request):
    page_title = "Home" # baru
    context_dict = {'title':page_title} # baru
    return render(request, 'main/index.html', context_dict) # baru
    

def about_view(request):
    page_title = "About" # baru
    context_dict = {'title':page_title} # baru
    return render(request, 'main/about.html', context_dict) # baru

