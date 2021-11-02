https://drive.google.com/file/d/1fkJcZ41SVNZk3ePIwa3FWDWHFB0JcMKi/view?usp=sharing
#Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
alphavit = 'abcdefgjihklmnopqrstuvwxyz'
a = input("Введите букву: ")
b = input("Введите букву: ")
r = alphavit.index(a)+1
t = alphavit.index(b)+1
print(r)
print(t)
print(abs(r-t)-1)
