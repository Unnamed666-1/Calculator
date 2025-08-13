x = int(input("Введіть x: "))
y = int(input("Введіть y: "))
n = int(input("Введіть n: "))

def Power(x, y):
    return pow(x, y) # повертаємо результат

print(Power(x, y))  # викликаємо функцію

def factorial(n):
    if n == 0 or n == 1:  # Базовий випадок: факторіал 0 або 1 дорівнює 1
        return 1
    else:
        return n * factorial(n - 1)  # Рекурсивний виклик

print(factorial(n))

def tetration(x, y):
    if y == 1:  # Базовий випадок: якщо степінь 1, повертаємо x
        return x
    elif x >= 4:
        print("Надзвичайно велике число")
    elif y >= 4:
        print("Надзвичайно велике число")
    else:
        return x ** tetration(x, y - 1)  # Рекурсивно підносимо до степеня
print(tetration(x, y))

def bowers_array(x, n, y):
    if n == 1:
        # Проста експоненціація
        return x**y
    elif y == 1:
        # Коли b = 1, повертаємо a, тетрація/пентація одного разу дорівнює самому числу
        return x
    elif n >= 3:
        print("Надзвичайно велике число")
    elif x >= 3:
        print("Надзвичайно велике число")
    elif y >= 3:
        print("Надзвичайно велике число")
    else:
        # Рекурсивне обчислення
        return bowers_array(x, n - 1, bowers_array(x, n, y - 1))

#Виводимо функцію
print(bowers_array(x, n, y))   
