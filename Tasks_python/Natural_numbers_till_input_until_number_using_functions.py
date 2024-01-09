def sum(x):
    if x==0:
        return 0
    else:
        return x+sum(x-1)

n=int(input('Enter the number: '))

print('Sum is : ', sum(n))
