from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
    path('register/', views.RegisterUser.as_view(), name='register'),  # регистрация
    path('login/', views.Login.as_view(), name='login'),  # аутентификация
    path('converter/', views.Converter.as_view(), name='converter'),  # заполнение формы для конвертера

]
