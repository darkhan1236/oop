class Task78a:
    def __init__(self, n, a):
        self.n = n
        self.a = a
    
    def calc(self):
        res = 1
        for i in range(n):
            res = res * a 
        return res
    
n = int(input("n = "))
a = int(input("a = "))
t = Task78a(n, a)
res = t.calc()
print(res)