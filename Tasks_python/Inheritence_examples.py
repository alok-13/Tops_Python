# Multilevel Inheritance

class Parent:
    def print(self):
        print("This is parent")


class Child1(Parent):
    def same1(self):
        print("This level 1")

class Child2(Child1):
    def same2(self):
        print("This level 2")

o1=Child2()
o1.same1()
o1.same2()
o1.print()

print("==================================")

# Hierarchical Inheritance

class Parent:
    def print(self):
        print("This is parent")

class Child1(Parent):
    def same1(self):
        print("This level 1")

class Child2(Parent):
    def same2(self):
        print("This level 2")
        
o1=Child1()
o2=Child2()
o1.same1()
o1.print()
o2.same2()
o1.print()
print("==================================")

# Hybrid Inheritance

class Parent1:
    def print1(self):
        print("This is parent1")

class Parent2:
    def print2(self):
        print("This is parent2")

class Child1(Parent1):
    def same1(self):
        print("This level 1-1")

class Child2(Parent1,Parent2):
    def same2(self):
        print("This level 1-2-1")

class Child3(Child2):
    def same3(self):
        print("This level 2-2-1")

class Child4(Child1):
    def same4(self):
        print("This level 2-1")

o1=Child4()
o2=Child3()
o1.same4()
o1.same1()
o1.print1()
print("====================================")
o2.same3()
o2.same2()
o2.print1()
o2.print2()




        
    
