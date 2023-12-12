# tasks/urls.py

from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView

urlpatterns = [
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_confirm_list"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("", TaskListView.as_view(), name="task_list"),
]
