from django.db import models


# Create your models here.

class DateConverter(models.Model):
    date_json = models.TextField(help_text='Строка с данными из запроса к API в виде строки json',
                                 verbose_name="Данные для конвертации")
