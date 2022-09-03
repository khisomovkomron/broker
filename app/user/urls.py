
from django.urls import path, include, re_path


urlpatterns = [
    
    re_path(r'^', include('dj_rest_auth.urls')),
    re_path(r'^registration', include('dj_rest_auth.registration.urls')),

]
