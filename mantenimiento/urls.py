from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("usuario/<int:pk>/", views.usuario, name="usuario"),
    path("equipo/<int:pk>/", views.equipo, name="equipo"),
    path("software/<int:pk>/", views.software, name="software"),
    path("driver/<int:pk>/", views.driver, name="driver"),
    path("revision/<int:pk>/", views.revision, name="revision"),
]
