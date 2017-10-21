from django.conf.urls import url
from . import views

app_name = 'todoapp'

urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^todolist/$', views.todolist.as_view(), name='todolist'),
    url(r'^todolist/(?P<pk>[0-9]+)/$', views.detail.as_view(), name='detail'),
]