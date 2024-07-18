from datetime import date

name = input("Enter the full name :")
birth_year = int(input("Enter the birthyear :"))

present_year = date.today().year - birth_year

print("Hello I am {} and I am {} years old".format(name,present_year),end=".")