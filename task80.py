class Task80:
    def __init__(self, x):
        self.x = x 
        
    def calc(self):
        res = 0
        f = 1  # Инициализация факториала
        deg = self.x  # Начинаем с x (x^1)
        sign = 1  # Начинаем с положительного знака
        
        for i in range(1, 14, 2):  # Проходим по нечетным индексам
            if i > 1:  # Для i = 1 (первое слагаемое, x) факториал = 1
                f *= i * (i - 1)  # Обновляем факториал для 3!, 5!, и т.д.
            res += sign * (deg / f)  # Добавляем текущее слагаемое с учетом знака
            deg *= self.x * self.x  # Умножаем на x^2 для следующего слагаемого
            sign *= -1  # Меняем знак

        return res
             
x = float(input("x = "))
t = Task80(x)
res = t.calc()
print(res)
