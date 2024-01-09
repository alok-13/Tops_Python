import math
r=int(input('Enter radius: '))
h=int(input('Enter height: '))
volume=math.pi*r*r*h
area=2*math.pi*r*(h+r)
print('Volume of Cylinder is: ',volume)
print('Surface area of Cylinder is: ',area)
