d1={'k1':5,'k2':2,'k3':7,'k4':1}
l1=[]
for i in d1.values():
    l1.append(i)

l1.sort(reverse=True)
print(l1[0:3])
