my_f = open("text.txt", "w")
content = input("введите что-нибудь: \n")
while content:
    my_f.writelines(content)
    content = input("введите что-нибудь: \n")
    if not content:
        break
print(content)
my_f.close()
