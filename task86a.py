class Task86a:
    def __init__(self, n):
        self.n = n
        
    def calc(self):
        length = 0
        n = self.n
        while n > 0:
            n = n // 10 
            length = length + 1 
        return length

n = int(input("n = "))
t = Task86a(n)
length = t.calc()
print(length)
