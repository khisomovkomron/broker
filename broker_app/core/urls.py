from django.contrib import admin
from django.urls import path
from broker_app.core.views import ListBroker

urlpatterns = [
    path("", ListBroker.as_view(), name='broker_app'),
]