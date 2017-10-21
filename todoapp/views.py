from django.views import generic
from django.views.generic.detail import DetailView

from .models import TodoItem


# from .forms import UserForm

# Create your views here.

class index(generic.TemplateView):
    template_name = 'todoapp/index.html'


class todolist(generic.ListView):
    template_name = 'todoapp/todolist.html'
    context_object_name = 'all_tasks'

    def get_queryset(self):
        return TodoItem.objects.all()


class detail(DetailView):
    template_name = 'todoapp/detail.html'

    model = TodoItem

    def get_context_data(self, **kwargs):
        context = super(detail, self).get_context_data(**kwargs)
        return context


