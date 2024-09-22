class Task86g:
    def __init__(self, n):
        self.n = n 
        
    def calc(self):
        sum = 0 
        for i in range(1, n + 1):
            if i % 2 == 0:
                sum -= i
            else:
                sum += i
        return sum
    
n = int(input("n = "))
t = Task86g(n)
res = t.calc()
print(res)