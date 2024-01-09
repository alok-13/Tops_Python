d1={'k1':1,'k2':4,'k3':9}
d2={'k1':1,'k2':5,'k5':1}


for k1,v1 in d1.items():
    for k2,v2 in d2.items():
        if k1==k2:
            d1[k1]+=d2[k2]

print(d1)
