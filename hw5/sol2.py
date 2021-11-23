"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент. Ваша программа
должна используя список имен участников выдать на выходе пары, кто и кому будет дарить, причем сам себе
человек не может подарить, дубликаты тоже не допустимы.
"""
import random

def santa(persons):
    print(persons)
    result={}
    for i in range(0, len(persons)):
        cel_santi=random.choice((persons[0:i]+persons[i+1:]))
        result[persons[i]]=cel_santi
    return result

persons=('Vlad', 'Sasha', 'Maria', 'Gena', 'Dasha')
result=santa(persons)
count=1
while result.setdefault(persons[-1])==None:
    count+=1
    result=santa(persons)
print(result)
print(count)