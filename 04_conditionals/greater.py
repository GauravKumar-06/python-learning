first_number=int(input("Enter a number ="))
second_number=int(input("Enter another number ="))

if first_number>second_number:
    print("{} is greater".format(first_number))
elif second_number>first_number:
    print("{} is greater".format(second_number))
else:
    print("The numbers are equal")

