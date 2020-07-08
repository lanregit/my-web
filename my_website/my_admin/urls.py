from django.urls import path
from my_admin import views

urlpatterns = [
    path('', views.index, name='admin'),
]