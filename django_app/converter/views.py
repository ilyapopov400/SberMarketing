from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

import json
from . import forms
from . import currency_converter
from . import models


# Create your views here.

class Index(TemplateView):
    '''
    Стартовая страница приложения converter
    '''
    template_name = "converter/index.html"


class RegisterUser(CreateView):
    '''
    Страница регистрации в приложении converter
    '''
    form_class = UserCreationForm
    template_name = "converter/register.html"
    success_url = reverse_lazy("converter:login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        """
        При успешной регистрации автоматически проводим аутентификацию
        и переходим на главную страницу приложения
        :param form:
        :return:
        """
        user = form.save()
        login(self.request, user)
        return redirect("converter:index")


class LoginUser(LoginView):
    '''
    Страница аутентификации в приложении converter
    '''
    form_class = AuthenticationForm
    template_name = "converter/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy("converter:index")


class LogoutUser(LogoutView):
    """
    Выход из идентификации пользователя
    """
    template_name = "converter/index.html"


class Converter(View):
    '''
    Заполнение формы для конвертера
    '''

    def get(self, request):
        form = forms.ConverterForm
        template_name = "converter/converter.html"
        context = {"form": form}
        return render(request=request,
                      template_name=template_name,
                      context=context)

    def post(self, request):
        model = models.DateConverter
        all_dates = model.objects.all()
        api_dict_today = json.loads(all_dates[0].date_json)

        template_name = "converter/result.html"
        form = forms.ConverterForm(request.POST)
        context = {}
        if form.is_valid():
            data = form.cleaned_data
            context["query_type_input"] = data.get("query_type_input")  # основная валюта
            context["query_type_output"] = data.get("query_type_output")  # валюта для перевода
            context["sum_of_money"] = data.get("sum_of_money")  # сумма исходная
            result = currency_converter.ParserCalculateConverter(
                query_type_input=context["query_type_input"],
                query_type_output=context["query_type_output"],
                sum_of_money=context["sum_of_money"],
                data_dict=api_dict_today,
            )()
            context["sum_of_result"] = round(result, 2)

        return render(request=request,
                      template_name=template_name,
                      context=context)
