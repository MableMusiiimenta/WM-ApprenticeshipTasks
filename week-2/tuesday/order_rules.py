def calculate_subtotal(price, quantity):
    return price * quantity

def is_valid_quantity(quantity):
    return quantity > 0
  
def is_product_available(product):
    return product["active"]

def has_enough_stock(stock, quantity):
    return stock >= quantity

def is_payment_complete(amount_paid, amount_due):
   return amount_paid >= amount_due

def can_place_order(
    product_available,
    valid_quantity,
    enough_stock,
    payment_ok,
):
    return (
        product_available
        and valid_quantity
        and enough_stock
        and payment_ok
    )

#input/data variables
def client_order():

    product = {
        "id": 1,
        "name": "Filter",
        "active": True,
        "stock": 3,
        "price": 80,
    }

    quantity = 2
    amount_paid = 160
    customer_is_member = True
    country = "DE"


# Calculated or derived values

    subtotal = calculate_subtotal(product["price"], quantity)
    is_given_discount = customer_is_member or subtotal >= 200
    if is_given_discount:

        final_total = subtotal - 10/100
        
        print(f" Only pay" + (""), str(final_total))
    else:
        final_total = subtotal - 0
        print("No discount")
  
    valid_quantity = is_valid_quantity(quantity)
    product_available = is_product_available(product)
    enough_stock = has_enough_stock(product["stock"], quantity)
  
    payment_ok = is_payment_complete(amount_paid, final_total)
  
# Final decisions

    order_proceeds = can_place_order(
        product_available,
        valid_quantity,
        enough_stock,
        payment_ok,
    )

    requires_manual_review = (subtotal > 500 or quantity > 5 or not payment_ok)
    
    gets_free_delivery = subtotal >= 100 and country == "DE"
    
    if order_proceeds:
        print("Order may proceed")
      
        if is_given_discount:
            print("You qualify for a discount")
          
        if gets_free_delivery:
            print("Goods can be delivered for free")
    else:
        print("Unable to place order")
  
        if not product_available:
            print("Product is not active")
        if not valid_quantity:
            print("Please enter a valid quantity")
        if not enough_stock:
            print("Not enough stock available")
        if not payment_ok:
            print("Please first complete payment")

    # if requires_manual_review:
    #   print("You may check with attendant")
    # else:
    #   if is_given_discount:
    #     print("You qualify for a discount")
    #   if gets_free_delivery:
    #     print("Goods can be delivered for free")
        
    if requires_manual_review:
        print("Order requires manual review")

client_order()




