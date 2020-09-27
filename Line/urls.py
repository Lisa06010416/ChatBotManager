from django.urls import path
from . import views

# app_name = "Line/"
urlpatterns = {
    path(r"lineCallBAck/", views.lineCallBAck, name="lineCallBAck"),
    path(r"getLinePage/", views.getLinePage, name="getLinePage"),
}