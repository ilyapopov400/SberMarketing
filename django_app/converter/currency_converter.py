from tmp_api_dict import api_dict


class ParserCalculateConverter:
    def __init__(self, data_dict: dict,
                 query_type_input: str, query_type_output: str,
                 sum_of_money: str):
        """
        преобразуем словарь из запроса и считаем результат конвертации валюты
        :param data_dict:
        :param query_type_input: валюта исходная
        :param query_type_output: валюта для перевода
        :param sum_of_money: денежная сумма
        """
        self.data_dict = data_dict
        self.query_type_input = query_type_input
        self.query_type_output = query_type_output
        self.sum_of_money = float(sum_of_money)

        self.data_dict["rates"]["RUB"] = self.data_dict["rates"]["RUB"] / 100  # ошибка на сайте

    def calculate(self):
        go_usd = self.data_dict.get("rates").get(self.query_type_input)  # перевели в доллары
        go_to_currency = self.data_dict.get("rates").get(
            self.query_type_output)  # с долларов перевели в заданную валюту

        return (self.sum_of_money / go_usd) * go_to_currency

    def __call__(self, *args, **kwargs):
        return self.calculate()


if __name__ == "__main__":
    result = ParserCalculateConverter(data_dict=api_dict, query_type_input="EUR",
                                      query_type_output="USD", sum_of_money="1")
    print(result())
