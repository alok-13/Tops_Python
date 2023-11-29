l1=[]
j=0
l2=[]
a=int(input("Enter length of list: "))
for i in range(0,a):  # INserting element in list
    n=input(f"Enter element number {i+1}: ")
    l1.append(n)
print(l1)

for i in l1: 
    if j==0:  # for zeroth index the value is directly added
        l2.append(i)

    else:
        if i in l2:  # if the current element is in the list then the element wont be added
            continue
        else:        # else it will added to the list
            l2.append(i)
    j+=1
print(l2) 
