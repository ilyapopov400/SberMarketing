from django import forms

currency_type = [
    ("USD", "доллар"),
    ("RUB", "рубль"),
    ("EUR", "евро"),

]


class ConverterForm(forms.Form):
    query_type_input = forms.ChoiceField(label="ваша валюта", choices=currency_type)
    query_type_output = forms.ChoiceField(label="перевод валюты", choices=currency_type)
    sum_of_money = forms.IntegerField(label="денежная сумма")
