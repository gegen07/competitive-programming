values = [100, 50, 20, 10, 5, 2, 1]

def getMoneyChange(money):
    times = []
    for num in values:
        times.append(int((money-money%num)/num))
        money -= times[len(times)-1] * num
    return times

money = int(input())
times = getMoneyChange(money)
i = 0
print(money)
for num in times:
    print("{0} nota(s) de R$ {1},00".format(num, values[i]))
    i+=1
