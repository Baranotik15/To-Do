from django.views.generic import TemplateView, ListView
from .models import Task, Tag


class HomePageView(TemplateView):
    template_name = 'core/home.html'


class TagListView(ListView):
    model = Tag
    template_name = 'core/tag_list.html'
    context_object_name = 'tag_list'

