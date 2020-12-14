my_strings = input("Введите предложение: ")
number = 1
a = []
for el in range(my_strings.count(' ') + 1):
    a = my_strings.split()
    if len(str(a)) <= 10:
        print(f" {number} {a [el]}")
        number += 1
    else:
        print(f" {number} {a [el] [0:10]}")
        number += 1

