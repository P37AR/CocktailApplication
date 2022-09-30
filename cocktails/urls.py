from django.urls import path

from cocktails import views

from .views import index

urlpatterns = [
    path("login", views.login_required, name="login"),
    path("", index),
    path("cocktails", views.cocktails, name="cocktails"),
    path("recipes", views.recipes, name="recipes"),
    path("videos", views.videos, name="videos")
]
