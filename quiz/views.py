from django.views import generic
from django.views.generic.detail import DetailView

class index(generic.TemplateView):
    template_name = 'quiz/index.html'