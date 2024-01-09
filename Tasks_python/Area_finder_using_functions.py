area=0
a=0
def area_finder(area):
    print('1. Circle\n2. Triangle\n3. Rectangle')
    n=int(input('Enter number: '))
    if n==1:
        r=int(input('Enter radius: '))
        a=3.14*r*r
        return a
    elif n==2:
        b=int(input('Enter base: '))
        h=int(input('Enter height: '))
        a=0.5*b*h
        return a
    elif n==3:
        b=int(input('Enter width: '))
        h=int(input('Enter height: '))
        a=b*h
        return a

print(area_finder(area))
    
