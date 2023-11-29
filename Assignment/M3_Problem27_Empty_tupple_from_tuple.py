t=(1,90,(),'sdd','',33,(1,3,5))
l=list(t)   # tuple to list because list has more in-built functions
for i in l:
    if i==():  # if the element contains an empty tuple it will be removed
        l.remove(i)
    
t=tuple(l)
print(t)

