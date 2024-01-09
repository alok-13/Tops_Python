l1=[]
j=0
l2=[]
a=int(input("Enter length of list: "))
for i in range(0,a):
    n=input(f"Enter element number {i+1}: ")
    l1.append(n)
print(l1)

for i in l1:
    if j==0:
        l2.append(i)

    else:
        if i in l2:
            continue
        else:
            l2.append(i)
    j+=1
print(l2)    

##l2.remove(65)
##l2.remove(12)
##l2.remove(34)

