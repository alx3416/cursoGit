import math


def getHypotenuse(side1, side2):
    hypotenuse = math.sqrt((side1 ** 2) + (side2 ** 2))
    return hypotenuse


def getRectangleArea(sideA, sideB):
    area = sideA * sideB
    return area


def getcircleArea(radius):
    area = math.pi * (radius ** 2)
    return area
