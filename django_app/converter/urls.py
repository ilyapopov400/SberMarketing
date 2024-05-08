from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы

]
