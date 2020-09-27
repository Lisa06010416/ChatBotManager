from django.urls import path
from . import views

# app_name = "Line/"
urlpatterns = {
    path(r"lineBroadCast/", views.lineBroadCast, name="lineBroadCast"),
    path(r"linePushMessage/", views.linePushMessage, name="linePushMessage"),
    path(r"lineCallBack/", views.lineCallBack, name="lineCallBack"),
    path(r"getLinePage/", views.getLinePage, name="getLinePage"),
}