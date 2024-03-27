from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('data/', views.welcome, name="data"),
  #  path('count_words/', views.count_words, name="count_words"),
]
