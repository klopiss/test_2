K = 1
while True:
    try:
        N = int(input("Введите целое положительно число N: ", ))
        break
    except ValueError:
        print ("Это не число, попробуйте ещё раз")
while N<=0:
    print ("Введите число больше нуля")
    N = int(input("Введите целое положительное число N: "))
while K*K<=N:
    K+=1
print(f"Наименьшее положительное целое чис5ло K, квадрат которого превосходит {N}, равно {K}.")