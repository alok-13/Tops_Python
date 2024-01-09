d1={'k1':1,'k2':4,'k3':9}
d2={'k1':1,'k2':5,'k5':1}
v=[]
a=0
b=0
c=0

k1= d1.keys()   # splitting keys and values in seperate list 
v1=d1.values()
k2= d2.keys()
v2=d2.values()

k1=list(k1)
v1=list(v1) 
k2=list(k2)
v2=list(v2)


for i in k1:
    b=0
    c=0
    for j in k2:   
        if i == j:   # comparing keys of both dictionaries 
            v.append(v1[a]+v2[b])  # adding values
            c+=1
        b+=1
    if c==0:
        v.append(v1[a])  # for distinct key value of first dictionary is added
    a+=1
    
d=dict(zip(k1,v)) 
print(d)
        
     




