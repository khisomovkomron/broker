from django.urls import path
from . import views

urlpatterns = [
    path("", views.SharesListCreateView.as_view()),
    path("<uuid:pk>", views.SharesRetrieveView.as_view()),
    path("del/<uuid:pk>", views.SharesDetailView.as_view()),
    path("modify/<uuid:pk>", views.SharesUpdateView.as_view()),
]