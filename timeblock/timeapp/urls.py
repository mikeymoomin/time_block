from django.urls import path
from . import views

app_name = "timeapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>",views.list_file, name="lists"),
    path("create", views.create, name="create"),
]