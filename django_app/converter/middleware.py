import requests
import json
import datetime
from . import models


class CheckApi:
    def __init__(self, get_response):
        self.get_response = get_response
        self.url = "https://open.er-api.com/v6/latest/USD"

    def __get_json(self) -> dict:
        """
        получаем json от API
        :return:
        """
        return json.loads(requests.get(self.url).text)

    def __change_datetime(self, renewal_day) -> bool:
        """
        проверяем сегодняшнюю дату и дату обновления

        :return:
        """
        renewal_day = renewal_day.split()[:-1]
        renewal_day = " ".join(renewal_day)
        now = datetime.datetime.now().date()
        renewal_day = datetime.datetime.strptime(renewal_day, "%a, %d %B %Y %H:%M:%S").date()

        return not (now < renewal_day)

    def __get_date(self):
        """
        работа с БД
        :return:
        """
        model = models.DateConverter
        all_dates = model.objects.all()
        if not bool(all_dates):
            # делаем первую запись в БД
            date_json = json.dumps(self.__get_json())
            record_obj = model(date_json=date_json)
            record_obj.save()
            print("Первая запись в БД")
        else:
            date = json.loads(all_dates[0].date_json)  # данные с БД
            time_next_update_utc = date.get("time_next_update_utc")  # дата следующего обновления курса
            if self.__change_datetime(renewal_day=time_next_update_utc):
                date_json = json.dumps(self.__get_json())  # данные о курсе валют
                record_obj = all_dates[0]
                record_obj.date_json = date_json
                record_obj.save()
                print("Обновленная запись в БД")
            else:
                print("Данные актуальны")

    def __call__(self, request):
        self.__get_date()
        response = self.get_response(request)
        return response


if __name__ == "__main__":
    pass
