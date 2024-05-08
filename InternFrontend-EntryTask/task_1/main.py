from data import encoded, translations


class Encoding:
    def __init__(self, encoded, translations):
        self.encoded = encoded
        self.translations = translations
        self.non_encoding = ["groupId", "service", "formatSize", "ca"]
        self.unicID = set()

    def _encod(self, part):
        result = dict()
        for key, value in part.items():
            if key in self.non_encoding:
                result[key] = value
            elif len(key) <= 2 or key[-2:].lower() != "id" or not value:
                result[key] = None
            else:
                if not isinstance(value, int):
                    value = int(value)
                result[key] = self.translations.get(value)
                self.unicID.add(key)
        return result

    def run(self):
        result = list()
        for part in self.encoded:
            result.append(self._encod(part))
        return dict(result=result, unicID=self.unicID)


if __name__ == "__main__":
    result = Encoding(encoded=encoded, translations=translations).run()

    print("Функция расшифровки полей с суффиксом id из переменной encoded")
    print(*result["result"], sep="\n")

    print("*" * 25)

    print("список уникальных id, из encoded")
    print(*result["unicID"])
