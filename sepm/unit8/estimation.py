class cocomo:
    a=0
    b=0
    c=0
    d=0
    def __init__(self, type):
        if type == 1:
            self.a,self.b,self.c,self.d = self.organic()
        elif type == 2:
            self.a,self.b,self.c,self.d = self.semiDetached()
        elif type == 3:
            self.a,self.b,self.c,self.d = self.embedded()
        
        

            
    def cocomo(self):
        """ """
        
    def organic(self):
        return (2.4, 1.05, 2.5, 0.38)

    def semiDetached(self):
        return (3.0, 1.12, 2.5, 0.35)        

    def embedded(self):
        return (3.6, 1.20, 2.5, 0.32)        

    

a = cocomo(1)
print(a.a)

