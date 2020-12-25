word = {
    "One": "1",
    "Two": "2",
    "Three": "3",
    "Four": "4"}
my_f = open("text3.txt", "r")
my_f1 = []
for i in my_f:
    i = i.split(None, 1)
    my_f1.append(word[i[0]] + i[1])
print(my_f1)
my_f.close()
my_f2 = open("text4.txt", "w")
my_f2.writelines(my_f1)
my_f2.close()
