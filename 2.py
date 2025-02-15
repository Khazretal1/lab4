import math

def area_trapezoid(h, b1, b2):
    return 0.5 * (b1 + b2) * h

height = float(input())
base1 = float(input())
base2 = float(input())
final = area_trapezoid(height, base1, base2)
print(f"Expected output: {final}")