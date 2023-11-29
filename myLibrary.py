import math


def getHypotenuse(sideB, sideA):
    hypotenuse = math.sqrt((sideA ** 2) + (sideB ** 2))
    return hypotenuse


def getRectangleArea(sideA, sideB):
    area = sideA * sideB
    return area


def getcircleArea(radius):
    area = math.pi * (radius ** 2)
    return area
