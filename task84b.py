import math

class Task84b:
    def __init__(self, x, n):
        self.x = x
        self.n = n 
        
    def calc(self):
        res = 0
        s = x
        for i in range(n):
            s = math.sin(s)
            res = res + s
        return res

x = int(input("x = "))
n = int(input("n = "))
t = Task84b(x, n)
res = t.calc()
print(res)