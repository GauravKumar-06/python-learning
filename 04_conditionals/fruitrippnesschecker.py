fruit_name = input("Enter the name of fruit :")
fruit_colour = input("Enter the present colour of fruit :").lower()

if fruit_colour =="green":
    print("{} is Unriped".format(fruit_name),end=".")
elif fruit_colour == "yellow":
    print("{} is Riped".format(fruit_name),end=".")
elif fruit_colour == "brown":
    print("{} is Overriped".format(fruit_name),end=".")
else:
    print("{} is in good condition".format(fruit_name),end=".")

