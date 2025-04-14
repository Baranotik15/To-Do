from django.urls import path

from .views import (
    HomePageView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    ToggleTaskStatusView,
)


app_name = "core"

urlpatterns = [
    # Task urls
    path(
        "",
        HomePageView.as_view(),
        name="home"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task_create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task_update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete"
    ),
    path(
        "tasks/<int:pk>/toggle/",
        ToggleTaskStatusView.as_view(),
        name="task_toggle"
    ),
    # Tag urls
    path(
        "tags/",
        TagListView.as_view(),
        name="tag_list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag_create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag_update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag_delete"
    ),
]
