from django.urls import path
from . import views

# app_name = "Line/"
urlpatterns = {
    path(r"lineBroadCast/", views.line_broadcast, name="line_broadcast"),
    path(r"linePushMessage/", views.line_push_message, name="line_push_message"),
    path(r"lineCallBack/", views.line_callback, name="line_callback"),
}