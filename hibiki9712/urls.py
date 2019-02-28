from django.urls import path, include
from django.contrib import admin

from .views import index, send_mail

urlpatterns = [
    path('', index, name="index"),
    path('send_mail', send_mail, name="send_mail"),
]
