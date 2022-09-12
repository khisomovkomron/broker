from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.BrokerListView.as_view()),
    path("<int:pk>/", views.BrokerDetailView.as_view()),
    path("apiview/", views.BrokerNestedView.as_view()),
]