a=open("Task.txt","w")
b=input("Enter text: ")
a.write(b)
print('Number of words are: ',len(b.split()))
a.close()
