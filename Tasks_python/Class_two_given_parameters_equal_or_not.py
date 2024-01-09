class Test:
    
    def __init__(self,x,y):

        self.a=x
        self.b=y

    def equal(self,c):
        if self.a==c.a and self.b==c.b:
            print('True')
        else:
            print('False')

o1=Test(4,5)
o2=Test(4,5)

o1.equal(o2)
