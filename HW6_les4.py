from itertools import count, cycle
for el in count(50):
    if el > 100:
        break
    else:
        print(el)
print('конец первой функции')
a = 0
for el in cycle("Geekbrains"):
    if a > 100:
        break
    print(el)
    a += 1
