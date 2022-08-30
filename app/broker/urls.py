from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.BrokerView.as_view()),
]