def findArea(r):
    PI = 3.14
    return PI * (r*r);
print("Area of circle = %.6f" % findArea(6));


import math
r = float(input("Enter the radius of a circle:"))
area = math.pi * r * r
print("Area of a circle = %.2f" %area)