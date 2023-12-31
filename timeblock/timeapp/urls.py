from django.urls import path
from . import views

app_name = "timeapp"
urlpatterns = [
    path("", views.index, name="index"),
    path('add/', views.add_task, name='add_task'),
    path('list/', views.task_list, name='task_list'),
    path('matrix/', views.matrix, name="matrix"),
]