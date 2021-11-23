"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
В результате ее работы на печать выводятся значения переданных переменных,
но только если они не равны None. Получим, например, следующее сообщение:
Переданы аргументы: var1 = 2, var3 = 10.
"""


def three_args(a=None, b=None, c=None):
    stroka = ""
    if a!=None:
        stroka = stroka + f"var1 = {a}"
    if b!=None:
        stroka = stroka + f"var2 = {b}"
    if c!=None:
        stroka = stroka + f"var3 = {c}"
    return stroka

print(three_args(a=6, b=7))