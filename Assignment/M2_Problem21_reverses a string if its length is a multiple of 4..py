a=0
l1=[]
l2=[]
s=input('Enter a string: ')
l1=s.split()
a=len(l1)
if a%4==0:
    l2=l1[::-1]
if len(l2)>0:
    s=''
    for i in l2:
        s=s+i+' '
  
print(s)
