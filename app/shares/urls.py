from django.urls import path
from . import views

urlpatterns = [
    path("", views.SharesListView.as_view()),
    path("<uuid:pk>/", views.SharesDetailView.as_view()),
]