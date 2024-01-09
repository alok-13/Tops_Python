a=int(input("Enter starting number: "))
b=int(input("Enter ending number: "))

j=0
k=a
l=[]
for l in range (a,b): 
    j=0
    for i in range (2,b):

        if l%i==0:
            print('Not prime')
            j+=1
            break
            
    if j==0:
        print(f'{l} is Prime ')
        l.append(l)
        
        
        
