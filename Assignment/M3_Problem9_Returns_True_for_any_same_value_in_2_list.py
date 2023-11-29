l1=[]
l2=[]
a=int(input("Enter length of list1: "))
for i in range(0,a):  # INserting element in list
    n=input(f"Enter element number {i+1}: ")
    l1.append(n)


b=int(input("Enter length of list2: "))
for i in range(0,b):  # INserting element in list
    m=input(f"Enter element number {i+1}: ")
    l1.append(m)


for i in l1:   # Assigning values of first list
    for j in l2:   # Assigning values of second list
        if i==j:   # comparing
            print("True")
