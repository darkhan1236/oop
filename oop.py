import math


class Task77g:
    def __init__(self, n):
        self.n = n
    
    def calc(self):
        res = 0
        sum = 0
        for i in range(1, n+1):
            sum = sum + math.sin(i)
            res = res + 1/sum
        return res

n = int(input("n = "))
task77g = Task77g(n)
res = task77g.calc()
print(res)