class Task82:
    def __init__(self, x):
        self.x = x
        
    def calc(self):
        res = 1 
        up = 1
        down = 1
        for i in range(1, 7):
            up = up * (x - 2 ** i)
            down = down * (x - 2 ** i - 1)
            res = res * up / down
        return res
    
x = int(input("x = "))
t = Task82(x)
res = t.calc()
print(res)