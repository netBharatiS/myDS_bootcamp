import math

####### calculate area of triangle

#input 3 sides of triangle
a, b, c = map(float, input("Enter length of three sides of Triangle: ").split())

# calculate semi perimeter s= (a+b+c)/2
s = ( a + b + c) / 2

print("Semiperimeter of triangle = " + str(s))

# calculate area of triangle Area = sqrt(s(s-a)*(s-b)(s-c))

temp = s * ((s - a) * (s - b) * (s - c))

area_triangle = math.sqrt(temp)

print("Area of triangle = " + str(area_triangle))
