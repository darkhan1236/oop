class Task86b1:
    def __init__(self, n):
        self.n = n 
    
    def calc(self):
        n = self.n 
        while n > 0:
            s = n % 10
            n = n // 10
        return s

n = int(input("n = "))
t = Task86b1(n)
s = t.calc()
print(s)                