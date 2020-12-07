firm_revenue = 1000000
firm_cost = 520000
people = 30
if firm_revenue > firm_cost:
    print("Компания работает в прибыль")
    print("рентабильность фирмы = " + str((firm_revenue - firm_cost) / firm_revenue * 100) + "%")
    print("прибыль на одного сотрудника составила " + str((firm_revenue-firm_cost) / people))
elif firm_cost > firm_revenue:
    print("Компания работает в убыток")
