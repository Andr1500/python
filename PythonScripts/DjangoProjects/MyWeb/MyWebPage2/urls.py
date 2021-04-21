from django.urls import include, path
from . import views  #import from the root directory

app_name = 'MyWebPage1'
urlpatterns = [
    path('', views.index, name='index'),
]