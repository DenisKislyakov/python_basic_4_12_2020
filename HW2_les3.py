name = input("Your name: ")
surname = input("Your surname:")
birthyear = int(input("Your birthyear: "))
city = input("Your city: ")
email = input("Your email: ")
phone = int(input("Your phone: "))
def person_info(name, surname, birthyear, city, email, phone):
    result = f" name - {name}, surname - {surname}, birthyear - {birthyear}, city - {city}, email - {email}, phone - {phone}"
    return result
print(person_info(name, surname, birthyear, city, email, phone))