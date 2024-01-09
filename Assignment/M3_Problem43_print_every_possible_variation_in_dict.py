d1={'1': ['a','b'], '2': ['c','d']}
v=0
a=0
v=d1.values()
l1=[]
l1=list(v)
print(l1)
for i in l1[0]:
    for j in l1[1]:
        a=i[0]+j[0]
        print(a)
    
