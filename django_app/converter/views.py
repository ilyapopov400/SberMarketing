from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from . import forms


# Create your views here.

class Index(TemplateView):
    '''
    стартовая страница приложения converter
    '''
    template_name = "converter/index.html"


class Converter(View):
    '''
    заполнение формы для конвертера
    '''
    def get(self, request, **kwargs):
        form = forms.ConverterForm
        template_name = "converter/converter.html"
        context = {"form": form}
        return render(request=request,
                      template_name=template_name,
                      context=context)

