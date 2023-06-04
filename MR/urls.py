from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.homepage, name="homepage"),
    path("Top", views.Top, name="Top"),
    path("<id>", views.Year, name="Year"),
    path("rating/<id>", views.rating, name="rating"),
]