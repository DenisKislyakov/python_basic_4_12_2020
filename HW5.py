distance_1 = 2
distance_2 = 5
day = 1
x = distance_1
while x < distance_2:
    x = x * 1.1
    day += 1
    print(str(day) + "-й день:" + str(x))
print("На " + str(day) + "-й день спортсмен достигнет результата не менее - " + str("%2d" % (x)) + " км")
