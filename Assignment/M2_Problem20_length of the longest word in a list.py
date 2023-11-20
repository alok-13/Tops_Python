l1=[]
a=0
b=0
s=input('Enter list: ')
l1=s.split()
for i in l1:
    a=len(i)
    if a>b:
        c=a
        d=i
    b=a
print('The largest word entered is: ',d)
