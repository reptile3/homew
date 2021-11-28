"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт, где на первом месте
номинал карты номинал (6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""

import random


def listn(n):
    chislo = random.choice(n)
    return chislo


def listm(m):
    figurka = random.choice(m)
    return figurka


if __name__ == "__main__":
    number = (6, 7, 8, 9, 10, "J", "D", "K", "A")
    mast = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    print(listn(number), listm(mast))