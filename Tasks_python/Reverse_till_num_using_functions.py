m=[]
def rev(x):
    if x==0:
        m.append(0)
    else:
        
        m.append(x)
        rev(x-1)
        
        
n=int(input('Enter the number: '))

rev(n)

print('Series is : ', m)
