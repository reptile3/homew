"""
Спортсмен поставил перед собой задачу пробежать в общей сложности Х километров.
В первый день спортсмен пробежал Y километров, а затем он каждый день увеличивал
пробег на 10% от предыдущего значения.
Определите номер дня в который спортсмен достигнет своей цели.
Оформите решение в виде программы, которая на вход принимает числа X и Y и выводит номер найденного дня.
"""


def sport(way, days):
    days.append(days[-1] + days[-1] * 1.1)
    if days[-1] >= way: return days
    return sport(way, days)


if __name__ == "__main__":
    way = int(input("All way, km: "))
    days = []
    days.append(int(input("Runed 1 day: ")))
    result = len(sport(way, days))
    print(f"All way runed for {result} days.")