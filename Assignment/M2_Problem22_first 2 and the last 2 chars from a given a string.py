z=''
s = input('Enter a string: ')

if len(s)<2:
    print('Empty string')
elif len(s)==2:
    print(s)
else:
    z=s[:2]+s[-2:-3:-1]+s[:-2:-1]
    print(z)
