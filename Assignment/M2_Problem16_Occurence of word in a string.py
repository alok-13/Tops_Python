s=input('Enter a string: ')
c=input('Enter word: ')
l1=[]
a=0
l1=s.split()
for i in l1:
    if c==i:
        a+=1
print(f'{c} is {a} time(s) in string')
