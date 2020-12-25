def sum1():
    my_f = open("text5.txt", "w")
    a = input("Введите числа: ")
    b = a.split()
    my_f.writelines(a)
    print(sum(map(int, b)))
sum1()
