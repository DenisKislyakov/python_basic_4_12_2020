https://drive.google.com/file/d/1fkJcZ41SVNZk3ePIwa3FWDWHFB0JcMKi/view?usp=sharing
#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
a = int(input("Введите первое трехзначное целое число: "))
b = int(input("Введите второе трехзначное целое число: "))
c = 0
d = 0
if a and b > 100 and a and b < 999:
    c = a + b
    d = a * b
    print (f'Сумма чисел равна: {c=}')
    print(f'Произведение чисел равно: {d=}')
else:
    print("Введены неправильные значени")
