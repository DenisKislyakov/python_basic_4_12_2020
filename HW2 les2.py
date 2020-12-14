some_list = []
i = 0
number = 0
while i < 5:
    a = input("Введите любое слово")
    some_list.append(a)
    print(some_list)
    i += 1
for el in range(int(len(some_list)/2)):
        some_list[number], some_list[number + 1] = some_list[number + 1], some_list[number]
        number += 2
print(some_list)

