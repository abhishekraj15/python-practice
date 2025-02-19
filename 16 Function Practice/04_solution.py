import math

def circle_stats(radius):
    area = math.floor(math.pi * radius ** 2)
    circumference = 2 * math.floor(math.pi * radius)
    return area, circumference


a, c = circle_stats(2)
print("Area :", a, "Circumfrance : ", c)