from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path("tasks/", views.view_tasks),
    path("add-task/", views.add_task),
    path("delete-task/<int:id>/", views.delete_task),
    path("complete_task/<int:id>/", views.complete_task),
    path("completed_tasks/", views.list_complete_task),
    path("admin/", admin.site.urls),
]
