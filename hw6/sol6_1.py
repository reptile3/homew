"""
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.
"""

import collections

def main(t):
    words = text.split() #разбивем текст на обьекты(слова)
    counter = collections.Counter(words) #делаем словарь и считаем обьекты
    most_common, kolichestvo = counter.most_common()[0] #выводит самое частое слово и как часто,
    # но почему-то как часто не показывает
    longest = max(words, key=len) # key должно показывать что ищем max именно по длинне

    result = f"часто встречающееся слово:{most_common}" \
             f"самое длинное слово:{longest}"
    return result

if __name__ == "__main__":
    text = "easy come easy go poslovica"
    print(main(text))