n=int(input('Enter a number: '))
i=1
l1=[]
while i<n:
    if n%i==0:
        l1.append(i)
    i+=1
if sum(l1)==n:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')
