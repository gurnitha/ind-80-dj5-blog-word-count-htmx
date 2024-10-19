# app/main/views.py

# Django modules
from django.http import HttpResponse
import datetime

# Create your views here.

def halodunia(request):
    now = datetime.datetime.now()
    html = "Halo Dunia! Waktu Jakarta sekarang adalah %s." % now
    return HttpResponse(html)

