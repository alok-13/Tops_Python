s=input('Enter string: ')

if len(s)<3:
    print(s)
else:

    if s[-1]=='g' and s[-2]=='n' and s[-3]=='i':
        print(s[:-3]+'ly')
    else:
        print(s[:-3]+'ing')
    
