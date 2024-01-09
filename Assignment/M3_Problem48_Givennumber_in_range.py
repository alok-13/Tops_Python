a=[1,2,3,4,5,6,7,8,9,10]
b=0
n=int(input('Enter a number: '))
for i in a:
    if n==i:
        print(f'{n} is in given range')
        b+=1
        break

if b==0:
    print(f'{n} is not in given range')
