from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.intres, name="intres"),
    path("search", views.search, name="search"),
    path('randompage', views.randompage, name="randompage" )
    ]
