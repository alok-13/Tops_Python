
# Ascending

d={'k1':1,'k2':5,'k3':7,'k4':4,'k5':6}
l=list(d.values())  
l.sort() # using list.sort() for sorting values
j=0
for i in l:      # assigning sorted value through a loop
    if j==0:       
        d['k1']=i
    if j==1:
        d['k2']=i
    if j==2:
        d['k3']=i
    if j==3:
        d['k4']=i
    if j==4:
        d['k5']=i
    j+=1   
        
print(d)

# Descending

d1={'k1':1,'k2':5,'k3':7,'k4':4,'k5':6}
l=list(d1.values())
l.sort(reverse=True) # for descending sorting
j=0
for i in l:     # assigning sorted value through a loop
    if j==0:
        d1['k1']=i
    if j==1:
        d1['k2']=i
    if j==2:
        d1['k3']=i
    if j==3:
        d1['k4']=i
    if j==4:
        d1['k5']=i
    j+=1   
        
print(d1)
