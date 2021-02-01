proseeds = int(input("Выручка фирмы: "))
costs = int(input("Издержки фирмы: "))
if proseeds < costs:
    print("Фирма работает в убыток")
else:
    print("Фирма работает с прибылью")
    profit = proseeds - costs
    profitability = profit / proseeds
    print("Рентабельность - ", profitability)
    employees = int(input("Количество сотрудников фирмы: "))
    pro_empl = profit / employees
    print("Прибыль фирмы в расчёте на одного сотрудника - ", pro_empl)