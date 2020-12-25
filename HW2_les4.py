list = [1, 4, 3, 8, 12, 1, 7, 325, 4, 2, 8]
print(f"Исходный список {list}")
new_list =[]
for el, i in enumerate(list):
    if list[el - 1] < list[el]:
        new_list.append(el)
print(f"Новый список {new_list}")
