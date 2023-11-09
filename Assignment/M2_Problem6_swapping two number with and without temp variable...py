#Problem 6.1
n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
temp=1
temp=n1
n1=n2

n2=temp

print(n1,n2)

#Problem 6.2

n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
print(f'old numbers are {n1} {n2} ')
n1=n1+n2
n2=n1-n2
n1=n1-n2
print(f'new numbers are {n1} {n2} ')
