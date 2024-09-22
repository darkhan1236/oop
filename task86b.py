class Task86b:
    def __init__(self, n):
        self.n = n 
    
    def calc(self):
        sum = 0
        n = self.n 
        while n > 0:
            sum = sum + n % 10
            n = n // 10
        return sum

n = int(input("n = "))
t = Task86b(n)
sum = t.calc()
print(sum)                