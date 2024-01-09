a=int(input("Enter a number: "))

j=0
for i in range (2,a):

    if a%i==0:
        print('Not prime')
        j+=1
        break
            
if j==0:
    print(f'{a} is Prime ')
