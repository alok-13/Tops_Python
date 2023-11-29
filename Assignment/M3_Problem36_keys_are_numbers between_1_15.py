d={}
d1={}
l=[]

for i in range(1,16,1): 
    if i==1:
        d={i:'a'}   # Assigning value of i from loop to key
    else:
        d1={i:'b'}
        d.update(d1)  # updating after every iterarion
print(d)
    
    
