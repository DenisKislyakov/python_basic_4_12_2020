my_f = open("text1.txt", "r")
content = my_f.readline()
print(f"строк {len(content)}")
my_f = open("text1.txt", "r")
content = my_f.read()
content = content.split()
print(f"количество слов {len(content)}")
my_f.close()


