from django.urls import path
from .import views

urlpatterns = [
    path('/', views.index),
    path('/reading', views.st_patty_page),
    path('/st_patty', views.st_patty)
]
