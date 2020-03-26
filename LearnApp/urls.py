from django.urls import path
from .import views

urlpatterns = [
    path('/', views.index),
<<<<<<< HEAD
    path('/reading', views.st_patty_page),
    path('/st_patty', views.st_patty)
=======
    path('/st_patty_page', views.st_patty_page),
    path('/gov_quiz_page', views.gov_quiz),
    path('/white_house_quiz_page', views.white_house),
    path('/declaration_quiz_page', views.declaration),
    # OUR GENERIC VALIDATOR
    path('/validate', views.generic_validator)
>>>>>>> 87bec6f33932028cf6bd289495183b326c190e45
]
