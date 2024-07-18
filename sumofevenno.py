number = int(input("Enter no. uo to which u want to add all the even numbers :"))
sum = 0
for i in range(1,number+1):
    if i % 2 == 0:
       sum = sum + i 
print(sum)
