from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reimagining", views.reimagining, name="reimagining"),
    path("global_children", views.global_children, name="global_children"),
    path("us_china", views.us_china, name="us_china"),
    path("environmental_stew", views.environmental_stew, name="environmental_stew"),
    path("gtr", views.gtr, name="gtr"),
    path("curriculum", views.curriculum, name="curriculum"),
    path("sig_ped", views.sig_ped, name="sig_ped"),
    path("books", views.books, name="books"),
    path("definition", views.definition, name="definition")
]