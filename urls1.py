from django.urls import path
from taskmanager import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
