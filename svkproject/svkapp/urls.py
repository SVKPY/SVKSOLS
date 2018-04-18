from django.conf.urls import url
import views

urlpatterns = [
        url(r'^index', views.index, name="index" ),
        url(r'^demo', views.demo, name="demo"),
        url(r'^todo',views.ToDo.as_view(), name='todo'),
        url(r'^todo/(?P<name>.*)$', views.ToDo.as_view(), name='todo')]