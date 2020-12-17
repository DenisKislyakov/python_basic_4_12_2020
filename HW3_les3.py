def fun(*numbers):
    number1 = int(input("Введите первое число "))
    number2 = int(input("Введите второе число "))
    number3 = int(input("Введите третье число "))
    if number1 > number3 and number2 > number3:
        return number1 + number2
    elif number2 > number1 and number3 > number1:
        return number2 + number3
    else:
        return number1 + number3
print(f'result - {fun()}')