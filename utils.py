import math

def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)  # 수정: math.squrt -> math.sqrt
    return c

def circle(r):
    area = math.pi * r**2
    return area
