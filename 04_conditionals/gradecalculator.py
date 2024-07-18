score = int(input("Enter the score :"))

if 100 >= score >= 90:
    print("Grade A")
elif 89 >= score >= 80:
    print("Grade B")
elif 79 >= score >= 70:
    print("Grade C")
elif 69 >= score >= 60:
    print("Grade D")
else:
    print("Fail")