#input/data variables
def client_order():

    product = {
        "id": 1,
        "name": "Filter",
        "active": True,
        "stock": 3,
        "price": 80,
    }


    quantity = 5
    amount_paid = 160
    customer_is_member = True
    country = "FR"


# Calculated or derived values

    subtotal = product["price"] * quantity
    valid_quantity = quantity > 0
    product_available = product["active"]
    enough_stock = product["stock"] >= quantity
    payment_ok = amount_paid >= subtotal

# Final decisions
    if not product_available:
        print("Item currently out of stock")
    else:
        if not valid_quantity:
            print("Please enter valid quantity")
        else:
            if not enough_stock:
                print("Not enough stock available")
            else:
                if not payment_ok:
                    print("Please first complete payment")

    if subtotal > 500 or quantity > 5 or not payment_ok:
        requires_manual_review = True
        

    if product_available and valid_quantity and enough_stock and payment_ok:
        print("Order May Proceed")
        if customer_is_member or subtotal >= 200:
            print("Qualifies for discount")
        else:
            print("0 discount")

        if subtotal >= 100 and country == "DE":
            print("Yay, Free delivery!")
        else:
            print("Pay for your own delivery")
    else:
        print("Unable to place order")
        

    print(requires_manual_review)
client_order()



