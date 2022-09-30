from django.urls import path, include

from authentication import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path("register", views.register_request, name="register"),
    path("cocktails", views.cocktails, name="cocktails")
]


