from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, Tag


class HomePageView(ListView):
    model = Task
    template_name = 'core/home.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    fields = ['content', 'deadline', 'tags']
    template_name = 'core/task_form.html'
    success_url = reverse_lazy('core:home')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['content', 'deadline', 'tags', 'is_done']
    template_name = 'core/task_form.html'
    success_url = reverse_lazy('core:home')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'core/task_confirm_delete.html'
    success_url = reverse_lazy('core:home')


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('core:home')


class TagListView(ListView):
    model = Tag
    template_name = 'core/tag_list.html'
    context_object_name = 'tag_list'


class TagCreateView(CreateView):
    model = Tag
    fields = ['name']
    template_name = 'core/tag_form.html'
    success_url = reverse_lazy('core:tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'core/tag_form.html'
    success_url = reverse_lazy('core:tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'core/tag_confirm_delete.html'
    success_url = reverse_lazy('core:tag_list')
