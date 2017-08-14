#manynames.py

x = 11

def f():
    print(x)

def g():
    x = 22
    print(x)

class C:
    x = 33
    def m(self):
        x = 44
        self.x = 55

if __name__ == '__main__':
    print(x)   #11: module
    f()        #11: global
    g()        #22: local
    print(x)   #11: module name unchanged
    
    obj = C()  #Make instance
    print(obj.x)  #33: class name inheritey by instance

    
    obj.m()   # Attach attribute name x to instance now
    print(obj.x) #55 instance
    print(C.x) #33 class(a.ka. obj.x if no x in instance)

    #print(C.m.x) #FAILS: only visible in method
    #print(g.x) #FAILS: ONLY VISIBLE IN FUNCTION
