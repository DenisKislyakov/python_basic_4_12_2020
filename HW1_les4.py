def fun_salary(): #production,  rate, prize, hour_per_week):
    production = int(input("Сколько сотрудник отработал часов: "))
    rate = int(input("Ставка на данного сотрудника: "))
    prize = int(input("Премия или штраф составил: "))
    hour_per_week = 40
    if production >= hour_per_week:
        result = (production * rate) + prize
        print(f"Сотрудник заработал: {result}")
    else:
        result1 = (production * rate) - prize
        print(f"Сотрудник заработал: {result1}")
fun_salary()
