seasons_list = ['лето', 'осень', 'зима', 'весна']
seasons_dict = {1 : 'лето', 2 : 'осень', 3 : 'зима', 4 : 'осень'}
while True:
    number_months = input("Введите номер месяца: ")
    if number_months.isdigit():
        number_months = int(number_months)
        break
    print("Ошибка! Введено не целое чилсло")
if number_months >= 6 and number_months <= 8:
    print("Вы выбрали " + seasons_dict.get(1))
    print("Вы выбрали " + seasons_list[0])
elif number_months >= 9 and number_months <= 11:
    print("Вы выбрали " + seasons_dict.get(2))
    print("Вы выбрали " + seasons_list[1])
elif number_months >= 3 and number_months <= 5:
    print("Вы выбрали " + seasons_dict.get(4))
    print("Вы выбрали " + seasons_list[3])
elif number_months == 12 or number_months <= 2:
    print("Вы выбрали " + seasons_dict.get(3))
    print("Вы выбрали " + seasons_list[2])
else:
    print("Ничего")
