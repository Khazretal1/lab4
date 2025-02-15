import math 

def degree_to_rad(degree):
    return degree * (math.pi / 180)

degree = float(input("Enter a degree: "))
radian = degree_to_rad(degree)

print(f"Input degree: {degree}\nOutput radian: {radian}")