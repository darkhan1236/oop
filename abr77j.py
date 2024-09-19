import math

class Task77j:
    def __init__(self, n):
        self.n = n 
        
    def calc(self):
        res = math.sqrt(3 * n) 
        for i in range(n-1, 0, -1): #генерирует последовательность чисел от start до stop (не включая stop), с шагом step.
            res = math.sqrt(3 * i + res)
        return res 

n = int(input("n = "))
t = Task77j(n)
res = t.calc()
print(res)
        