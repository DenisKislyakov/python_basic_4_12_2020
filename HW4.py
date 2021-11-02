https://drive.google.com/file/d/1fkJcZ41SVNZk3ePIwa3FWDWHFB0JcMKi/view?usp=sharing
#Определить, является ли год, который ввел пользователь, високосным или не високосным.
year = int(input("Введите год: "))
if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
    print("Год високосный")
else:
    print("Год не високосный")
