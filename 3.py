import math

def polygon_area(sides, length):
    if sides < 3:
        raise ValueError("Need more than 3 sides")
    return int((sides * length ** 2) / (4 * math.tan(math.pi / sides)))


sides = int(input("Input number of sides: "))
length = float(input("Input the lenght of sides: "))
area = polygon_area(sides, length)
print(area)
