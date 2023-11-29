l1=[]
l2=[]
a=int(input("Enter length of list1: "))
for i in range(0,a):  # Inserting element in list
    n=input(f"Enter element number {i+1}: ")
    l1.append(n)

s1=set(l1)  # typecasting list to set
l2=list(s1) # typecasting set to list
print(l2)
