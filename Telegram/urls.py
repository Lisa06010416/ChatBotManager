from django.urls import path
from . import views

# app_name = "Telegram/"
urlpatterns = [
    path(r"webhook/", views.webhook_handler, name="webhook_handler")
]
