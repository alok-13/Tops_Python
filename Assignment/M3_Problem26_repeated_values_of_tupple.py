t=(1,2,2,3,4,5)
s=set(t) # converting tuple to set because set does not allow duplicate values
t1=tuple(s) # converting set to tuple  

if len(t)>len(s): # comparing lengths of 2 tuples to check for duplication
    for i in range (0,len(t)-1):
        if t[i]!=t1[i]:   # if elements of first tuple and second tuple dont match that particular element will be printed 
            print(f'{t1[i-1]} is repeated')
            break
else:
    print('No duplicate values')
                

