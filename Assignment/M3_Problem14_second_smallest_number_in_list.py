l1=[5,4,2,6,9,1,3,2]
l2=[]
for i in l1:
    if i > min(l1):
        l2.append(i)  # removing min of the list and creating a seperate list 
        
print(min(l2))                
