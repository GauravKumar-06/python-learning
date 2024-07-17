sp=int(input("Enter selling price: "))
cp=int(input("Enter cost price: "))

# print(type (sp))

if sp>cp:
    profit = sp-cp
    print("The profit is: ",profit)
elif cp>sp:
    loss=cp-sp;
    print("The loss is: ",loss)
else:
    print("Neither profit nor loss")


print("Final code")