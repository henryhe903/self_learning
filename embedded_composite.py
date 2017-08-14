# File person.py

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return '[Person: %s,%s]' % (self.name, self.pay)

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
        
    def giveRaise(self,percent,bonus=0.10):
        self.person.giveRaise(percent+bonus)

    def __getsttr__(self, attr):
        return getattr(self.person,attr)

    def __str__(self):
        return str(self.person)
        

if __name__ == '__main__':
    
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev',pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(),sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    #print(tom.lastName())
    print(tom)
    print('--All There--')
    for object in (bob, sue, tom):
        object.giveRaise(.10)
        print(object)

    class Department:
        def __init__(self, *args):
            self.members = list(args)
        def addMember(self,person):
            self.members.append(person)
        def giveRaise(self,percent):
            for person in self.members:
                person.giveRaise(percent)
        def showAll(self):
            for person in self.members:
                print(person)

    development = Department(bob,sue)
    development.addMember(tom)
    development.giveRaise(.10)
    development.showAll()
              

             
