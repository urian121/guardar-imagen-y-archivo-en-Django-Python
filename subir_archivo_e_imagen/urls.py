from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("upload", views.upload, name="upload"),
    path("lista-de-registros/", views.listarData, name="listarData")
]
