from django.urls import path
from . import views

urlpatterns = [
    path("LiaIA/", views.acessarIA, name="liaia"),
    path("chat/", views.chat_api, name="chat"),
]