class Calculator:
    def __init__(self):
        self.current_num = 0

    def plus(self, x):
        self.current_num += x
        
    def minus(self, x):
        self.current_num -= x
        
    def multiply(self, x):
        self.current_num *= x
        
    def double(self):
        self.current_num *= 2
        
    def triple(self):
        self.current_num *= 3
        
    def show(self):
        print(self.current_num)


"""
We will judge your code using following scripts
"""
#my_calculator = Calculator()
#while True:
#    try:
#        cmd, *args = input().split()
#        if cmd == "plus":
#            my_calculator.plus(int(args[0]))
#        elif cmd == "minus":
#            my_calculator.minus(int(args[0]))
#        elif cmd == "multiply":
#            my_calculator.multiply(int(args[0]))
#        elif cmd == "double":
#            my_calculator.double()
#        elif cmd == "triple":
#            my_calculator.triple()
#        elif cmd == "show":
#            my_calculator.show()
#    except:
#        break
