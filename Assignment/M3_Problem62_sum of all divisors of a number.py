n=int(input('Enter a number: '))
i=1
l1=[]
while i<n:
    if n%i==0:
        l1.append(i)
    i+=1
print('Sum of all divisors: ',sum(l1))
