from django.urls import path
from . import views

urlpatterns = [
    path("", views.SharesListCreateView.as_view()),
    path("retrieve/", views.SharesRetrieveView.as_view()),
    path("del/<uuid:pk>", views.SharesDetailView.as_view()),
    path("update/", views.SharesUpdateView.as_view()),
]