l1=[]
s=input('Enter string: ')
t=input('Enter string which needs to be inserted: ')
l1=s
a=len(l1)
print(l1)


if a%2==0:
    l1[(a/2)::1]=t
else:
    l1[(a+1)/2::1]=t
