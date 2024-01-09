s=input('Enter a string: ')
l1=list(s)
l2=l1[::-1]
if l1==l2:
    print(f'{s} is a palindrome')
else:
    print(f'{s} is not a palindrome')

