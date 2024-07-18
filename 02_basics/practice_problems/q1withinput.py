Total = int(input("Enter the total items bought :"))
Sale = int(input("Enter the total items sold :"))
Price_per_item = int(input("Enter the price of one item :"))  

Items_left = Total - Sale
Total_earnings = Sale * Price_per_item

print("No. of items left for sell is",Items_left,end=".")
print("Total money earned by selling {} items is :".format(Sale),Total_earnings,end=".")