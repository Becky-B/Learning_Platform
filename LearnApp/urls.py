from django.urls import path
from .import views

urlpatterns = [
    path('/', views.index),
#     path('', views.history),
#     path('gov_quiz', views.gov_quiz),
#     path('white_house', views.white_house),
#     path('declaration', views.declaration)
]
