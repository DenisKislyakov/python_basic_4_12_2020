list = [50, 26, 1, 9, 50, 4, 5, 7, 50]
new_list = []
print(f"Исходный список {list}")
for el, i in enumerate(list):
    element_under_inspection = list[0]
    list.remove(element_under_inspection)
    if element_under_inspection not in list:
        new_list.append(element_under_inspection)
    list.append(element_under_inspection)
print(f"Результат {new_list}")
