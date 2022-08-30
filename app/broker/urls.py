from django.urls import path, include
from views import BrokerView

urlpatterns = [
    path("", BrokerView.as_view(), name='broker'),
]
