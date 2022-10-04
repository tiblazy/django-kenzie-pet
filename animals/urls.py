from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.AnimalMultiplyView.as_view()),
    path('animals/<int:animal_id>/', views.AnimalUpdateView.as_view())
]