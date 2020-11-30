from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_todo, name="index"),
    path('update/<int:id>', views.update_todo, name="update"),
    path('delete/<int:id>', views.delete_todo, name="delete"),
]
