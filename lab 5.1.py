first_deposit = 1000
x = 1100
results = []
for P in range(1,25):
    percent = P / 100
    deposit = first_deposit
    months = 0
    while deposit <=x:
        deposit += deposit*percent
        months +=1
    results.append((P, months, round(deposit, 2)))
for result in results:
    P, months, final_deposit = result
    print(f"При P={P}% вклад превысит 1100 рублей за {months} месяцев, итоговый вклад будет составлять: {final_deposit}")