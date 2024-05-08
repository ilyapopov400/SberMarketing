import requests
import json


class Converter:
    url = "https://open.er-api.com/v6/latest/USD"

    def __init__(self):
        self.__result = json.loads(requests.get(self.url).text)
        self.time_last_update_utc = self.__result.get("time_last_update_utc")
        self.base_code = self.__result.get("base_code")
        self.result_date = self.__result.get("rates")


if __name__ == "__main__":
    print("Hello World!!!")
    result = Converter()
    print(result.time_last_update_utc)
    print(result.base_code)
    print(result.result_date)
