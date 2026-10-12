# which variables you think you need;
# quantity, enough_stock(boolean), totalPrice

# what values they should initially contain;
# quantity is 2, enough stock is a boolean to compare stock to quantity, totalPrice stores the product of price and quantity

# which expression will calculate the price;
#multiplication(*) will calculate the price

# which expression will determine whether enough stock exists.
#greater than or equal to (>=) will determine whether enough stock exists


product = {
    "name": "Filter",
    "price": 80,
    "stock": 1,
}
qty=2

totalPrice = product["price"]*qty
enough_stock = product["stock"] >= qty
if enough_stock:
    print(totalPrice)
else:
    print("Not enough stock")

