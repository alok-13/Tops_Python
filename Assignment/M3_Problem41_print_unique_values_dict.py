d1={'k1':1,'k2':2,'k3':5,'k4':4,'k5':2}
a=0
b=0
l1=[]
s1=()

for i in d1.values():       # Assigning value of  dictionary
    l1.append(i)            # appending each element to list
s1=set(l1)                  # Typecating list to a set
print(s1)

