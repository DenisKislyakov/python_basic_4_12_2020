my_f = open("text6.txt","r")
my_f1 = []
for i in my_f:
    i = i.split()
    if int(i[1]) < 20000:
        my_f1.append(i[0])
print(f"у сотрудника {my_f1} зарпалата меньше 20000")