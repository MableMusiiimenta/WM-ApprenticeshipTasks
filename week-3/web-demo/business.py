def calculate_subtotal(price, quantity):
    return price * quantity

def is_valid_quantity(quantity):
    return quantity > 0 < 15
  
def is_product_available(product):
    return product["active"]

def has_enough_stock(stock, quantity):
    return stock >= quantity

def is_payment_complete(amount_paid, amount_due):
    return amount_paid >= amount_due