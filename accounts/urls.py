from django.urls import path
from .views import user_login


urlpatterns=[
    path("bi-login/", user_login, name='login'),
]