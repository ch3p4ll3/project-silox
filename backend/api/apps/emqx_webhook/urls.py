from django.urls import path
from django.conf.urls import include
from .views import EmqxWebhoox


urlpatterns = [
    path('', EmqxWebhoox.as_view()),
]
