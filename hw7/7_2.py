"""
Дан список стран и городов каждой страны, где ключи это названия стран,
а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну.
Оформить в виде программы, которая считывает название города и выводит на печать страну.
"""


def strani_goroda(gorod):
    country_city = {"USA":("New-York", "Minisota",), "Belarus":("Minsk", "Brest", "Gomel")}
    for key, value in country_city.items():
        if gorod in value:
            return key


if __name__ == "__main__":
    gorod = input("Type city name: ")
    print(strani_goroda(gorod))
