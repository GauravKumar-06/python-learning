items_bought = 1300
items_sold = 400
price_of_each_item = 15

items_left = items_bought-items_sold
total_earnings = items_sold*price_of_each_item

print("No of items in stock: ",items_left)
print("Total money earned by selling {} items is".format(items_sold),total_earnings,end=".")
