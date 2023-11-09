#Problem 3

a=int(input("Enter a number: "))
b=0
i=1
c=1
d=1
while i<=a:
    b=c
    c=d
    if i==1:
        b=0
        i+=1
        print(b)
    elif i==2:
        b=1
        i+=1
        print(b)
    else:
        d=b+c
        i+=1
        print(d)
