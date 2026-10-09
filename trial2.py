payments = [
    {"name": "A", "amount": 100},
    {"name": "B", "amount": -20},
    {"name": "C", "amount": "50"},
    {"name": "D", "amount": 25.5},
]

def validate_amount(value):

    if isinstance(value, bool):
        return False

    if not isinstance(value, (int,float)):
        return False
    if value < 0:
        return False

    return True

def check_payments():
    list1 = []
    total = 0
    payments = [
    {"name": "A", "amount": 100},  #i expect this to return True because it is an integer greater than 0 so the loop skips all conditions that return False to the last return statement which is True

    {"name": "B", "amount": -20}, #i expect this to return False because it meets the 3rd if which calls for numbers less than 0 to return False

    {"name": "C", "amount": "50"},  #i expect this to return False because it is a string and it meets the 2nd if which calls for values that are neither integers or floats to return False

    {"name": "D", "amount": 25.5}, #i expect this to return True because it is a float greater than 0 so the loop skips all conditions that return False to the last return statement which is True

    {"name": "E", "amount": True},  #i expect this to return False because it is a boolean and it meets the 1st if which calls for values that are booleans to return False 
]
    for payment in payments:
        for key, value in payment.items():
            print(validate_amount(value))
            if validate_amount(value) is True:
                list1.append(value)
                total += value
    print(list1)
    print(total)
check_payments()






# print(payments)   





# The business rule is:

# A valid amount must be an int or float, must not be a Boolean, and must be zero or greater.

# Before you code, write down for each record whether you expect the amount to be valid or invalid, and why.

# Then implement:

# validate_amount(value)

# The function should return only:

# True
# or
# False



# Then use the result of validate_amount() so that invalid amounts are not included in the total.

# Your final accepted total should only contain the valid amounts.

# Important: do not simply call the validation function and then continue calculating anyway. Think about how the returned True or False has to influence the next step of the program.

# We only want to add valid monetary amounts. A valid amount must be an int or float, must not be a Boolean, and must be zero or greater.
# Don't code immediately. First tell me what should happen to each record.