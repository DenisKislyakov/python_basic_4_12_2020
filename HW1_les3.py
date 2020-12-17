def fun(*numbers):
    number1 = int(input("Введите первое число "))
    number2 = int(input("Введите второе число "))
    if number2 != 0:
        return number1 / number2
    else:
        print("Error")
print(f"result  {fun()}")

