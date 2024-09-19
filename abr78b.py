class Task78b:
    def __init__(self, n, a):
        self.n = n 
        self.a = a
        
    def calc(self):
        res = a +  n - 1
        for i in range(n):
            res = (a*(a + 1)) * res
        return res
    
n = int(input("n = "))
a = int(input("a = "))
t = Task78b(n, a)
res = t.calc()
print(res)