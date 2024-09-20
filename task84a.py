import math

class Task84a:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def calc(self):
        res = 0 
        for i in range(1, n+1):
            res = res + math.sin(x) ** i    
        return res

x = int(input("x = "))
n = int(input("n = "))
t = Task84a(x, n)
res = t.calc()
print(res)
                