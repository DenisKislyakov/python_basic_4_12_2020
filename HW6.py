user_number = 1241724912412
r = 0
while user_number > 0:
    d = user_number % 10
    user_number //= 10
    if d >= r:
        r = d
print(r)