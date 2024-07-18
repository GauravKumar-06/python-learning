weather_status = input("Enter the current weather status :")

if weather_status == "Sunny" or "sunny":
    print("Go for a walk",end=".")
elif weather_status == "Rainy" or "rainy":
    print("Read a book",end=".")
elif weather_status == "Snowy" or "snowy":
    print("Build a snowman",end=".")
else:
    print("Jo krna hai kr dimag mt kha",end=".")