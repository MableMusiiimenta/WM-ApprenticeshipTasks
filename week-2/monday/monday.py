def valid_amount(value):
    if not isinstance(value, (int, float)):
        return False

    if value < 0:
        return False

    return True


amount = -25
result = valid_amount(amount)

print(result)


name = "Amina"
age = 4
fee = 120000.0
registered = True
notes = None

old_age = age
age = 6

value = "120"
value = int(value)

expected = 120
paid = 80

outstanding = expected - paid



total = 10 + 5 * 2

total = (10 + 5) * 2


age = 20
is_adult = age >= 18

expected = 100
paid = 120
overpaid = paid > expected


price = 100
discount = 70

final_price = price - discount

is_expensive = final_price > 50

if is_expensive:
    category = "high"
else:
    category = "low"

print(final_price)
print(is_expensive)
print(category)