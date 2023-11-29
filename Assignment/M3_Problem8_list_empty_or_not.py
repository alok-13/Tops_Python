l1=[]
a=int(input("Enter length of list: "))
for i in range(0,a):  # INserting element in list
    n=input(f"Enter element number {i+1}: ")
    l1.append(n)
if len(l1)==0:    # length of l1 = 0 then it will print list is empty
    print("list is empty")
