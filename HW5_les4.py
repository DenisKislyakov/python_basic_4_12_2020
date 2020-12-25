from functools import reduce
def my_func(prev_el, el):
    return prev_el * el
print(f'произведение: {reduce(my_func, [el for el in range(10,1002,2)])}')
