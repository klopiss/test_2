import math
while True:
    try:
        x = float(input("Введите действительное число x: ", ))
        break
    except ValueError:
        print ("Это не число, попробуйте ещё раз")
while True:
    try:
        n = int(input("Введите натуральное число n: ", ))
        break
    except ValueError:
        print("Это не число, попробуйте ещё раз")
while n<=0:
    print ("Введите число больше нуля")
    n = int(input("Введите целое положительное число n: "))
def sum(x,n):
    result = 0
    for i in range(1, n+1):
        y = x**i / math.factorial(i)
        result += y
    return result
result = sum(x, n)
print(f"Сумма ряда для x = {x} и n = {n} равна: {result}")