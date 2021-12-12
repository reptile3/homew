"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. 
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности), 
Triangle (атрибуты: три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и периметра). 
При потребности создавать все необходимые методы не описанные в задании. 
"""
"""
import math as m


class Point:
    def init(self,x1,y1,x2,y2,x3,y3):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
        
    def get_first_side(self):
        a=m.sqrt((self.x2 - self.x1)**2+(self.y2-self.y1)**2)
        return a 
        
    def get_second_side(self):
        b=m.sqrt((self.x2 - self.x3)**2+(self.y2-self.y3)**2) 
        return b
        
    def get_third_side(self):
        c=m.sqrt((self.x3 - self.x1)**2+(self.y3-self.y1)**2)
        return c


class Figure:
    pass


class Circle(Figure):
    def init(self,center,radius):
        self.center=center
        self.radius=radius


    def get_perimeter(self):
        perimeter=2*self.radius*m.pi
        return perimeter
        
"""