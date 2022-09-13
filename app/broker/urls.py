from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(prefix='viewset', viewset=views.BrokerViewSet, basename='viewset')

urlpatterns = [
    path("", views.BrokerListView.as_view()),
    path("<int:pk>/", views.BrokerDetailView.as_view()),
    path("apiview/", views.BrokerNestedView.as_view()),
    path('', include(routers.urls))
]