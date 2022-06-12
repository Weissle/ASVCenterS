from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('login', views.login_view, name='login_view'),
]
