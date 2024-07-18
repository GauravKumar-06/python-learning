fruit_name = input("Enter the name of fruit :")
fruit_colour = input("Enter the present colour of fruit :")

if fruit_colour == "Green" or fruit_colour =="green":
    print("{} is Unriped".format(fruit_name),end=".")
elif fruit_colour == "Yellow" or fruit_colour == "yellow":
    print("{} is Riped".format(fruit_name),end=".")
elif fruit_colour == "Brown" or fruit_colour == "brown":
    print("{} is Overriped".format(fruit_name),end=".")
else:
    print("{} is in good condition".format(fruit_name),end=".")

