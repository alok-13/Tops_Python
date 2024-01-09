q ={}
##k=[]
##a=[]
points=0

for i in range (0,2):
    qx={}
    que=input(f'Enter Question{i+1}: ')
    ans = input(f'Enter Answer{i+1}: ')
    qx = {'Question':que,'Answer':ans}
    q[f'ques {i+1}']=qx
    



print(q)


##for i,j in q.items():
##    k.append(j['Question'])
##    a.append(j['Answer'])
    

for i in range(0,2):    
    print('first question: ',q[f'ques {i+1}']['Question'])
    a1=input('Enter answer: ')
    if a1==q[f'ques {i+1}']['Answer']:
        print('Correct Answer \n +10 points')
        points+=10
    else:
        print('Wrong Answer \n -5 points')
        points-=5

print('\nTotal points: ',points)



