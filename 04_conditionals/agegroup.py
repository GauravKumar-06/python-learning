age = int(input("Enter the age ="))

if age < 13:
    print("Above mentioned person's age group is Child",end=".")
elif age <=19:
    print("Above mentioned person's age group is Teenager",end=".")
elif 20<=age<=59:
    print("Above mentioned person's age group is Adult",end=".")
else:
    print("Above mentioned person's age group is Senior",end=".")
