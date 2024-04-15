
#Task 12


menu = ["Tea", "Americano", "Latte", "Expresso", "Cake", "Cookies"]                                       # List of menus
total_stock = 0.00
total_value = 0.00

stock = { 'Tea' : 10,                                                                                     # Stock of items
          'Americano' : 20,
          'Latte' : 50,
          'Expresso' : 15,
          'Cake' : 17,
          'Cookies' : 23
          }

price = { 'Tea' : 2.99,                                                                                     # price of items
          'Americano' : 3.50,
          'Latte' : 3.00,
          'Expresso' : 2.50,
          'Cake' : 1.89,
          'Cookies' : 1.50
          }
print("**********************************************************************************************")
print("Cafe menu card:")                                                                     # print list of items with price
print(price)
print("**********************************************************************************************")

for key, value in stock.items():                                                             # for each item in stock 
    item_price = price.get(key)                                                                # find the price of the item from dict price[]
    item_value = value * item_price                                                            # value is stock of item in stock[], calculate total value of item 
    total_stock =  total_stock + item_value                                                    # add up total value of all items in stock
    print(f"{key} value = {item_value}")                                                       # print value of each item in the stock
  

print("*********************************************************************************************")
print(f"Total stock value of the cafe is {total_stock} pounds")                             # print the total stock value in the cafe 
print("*********************************************************************************************")