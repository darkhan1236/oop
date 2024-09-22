class Task78b1:
    def __init__(self, n, a):
        self.n = n
        self.a = a
        
    def calc(self):
        res = 1/a
        s = 1
        for i in range(n):
            s = s * (a + n)
            res = res + 1 / a * s
        return res
    
n = int(input("n = ")) 
a = int(input("a = "))
t = Task78b1(n, a)
res = t.calc()
print(res)