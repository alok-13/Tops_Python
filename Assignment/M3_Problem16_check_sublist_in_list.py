l1=[1,[2,4,6],8,4,9,36,25,4]
a=0
for i in l1:   # Assigning individual elements of l1 to i
    if type(i)==list: # using type() function to check type of each element  
        print('List contains a sublist')
        a+=1
        break
   
        
