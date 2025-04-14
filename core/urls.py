from django.urls import path

from .views import HomePageView, TagListView


app_name = "core"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tags/', TagListView.as_view(), name='tag_list'),
]
