from oops import Caculator


class A(Caculator):
    num2= 200

    def __init__(self):
        Caculator.__init__(self, 10)
    
    def getcompletedata(self):
        print(self.num2 + self.num)

        
obj= A()
obj.getcompletedata()
obj.getdata()
