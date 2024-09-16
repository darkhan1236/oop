import math

class Task77e:
    def __init__(self, n):
        self.n = n
        
    def calc(self):
        res = 1
        s1 = 0
        s2 = 0 
        
        for i in range(1, n+1):
            s1 = s1 + math.cos(i)
            s2 = s2 + math.sin(i)
            res = res*(s1/s2)
        return res
    
n = int(input("n = "))
t = Task77e(n) # класстын обьектиси
res = t.calc() # таск77е нын методын шакырып турмыз
print(res)
            