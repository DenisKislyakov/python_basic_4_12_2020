https://drive.google.com/file/d/1fkJcZ41SVNZk3ePIwa3FWDWHFB0JcMKi/view?usp=sharing
#По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x1=int(input("Первая координата х1: "))
y1=int(input("вторая координата y1: "))
x2=int(input("Первая координата х2: "))
y2=int(input("Первая координата y2: "))
k=(y1-y2)/(x1-x2)
b=y1-x1*k
print(f'y={k}x+{b}')
