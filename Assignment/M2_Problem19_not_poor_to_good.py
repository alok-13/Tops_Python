

l1=[]
a=0
i=0
y=0
j=0
f=0
b=0
x=''
s=input('Enter string: ')
n=len(s)
l1=s.split()
for i in l1:
    if i=='poor':
        b=y
        if x=='not':
            a=y
            l1.remove('not')
            l1.remove('poor')
            l1.insert(y,'good')
    if x=='not':
        f=y
    x=i
    y+=1
if a>0:
    print('The index of not is : ',a-1)
    print('The index of poor is : ',a)
if b>0 and a==0:
    print('The index of poor is : ',b)
if f>0 and b==0:
    print('The index of poor is : ',f-1)    
s=''
for j in l1:
    s=s+j+' '
print(s)


