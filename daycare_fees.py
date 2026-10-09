def validate_amount(value):
    
    
    if not isinstance(value, (int, float)):
            return False

    if value < 0:
         return False

    return True

def calculate_totals():

    payments = [    {"baby": "Amina", "expected": 120000, "paid": 120000},    {"baby": "Joel", "expected": 120000, "paid": 80000},    {"baby": "Grace", "expected": 150000, "paid": 0},    {"baby": "Amina", "expected": 50000, "paid": 50000},]

    for payment in payments:
        print(payment["expected"])
        
        print(payment["paid"])
        print(validate_amount(payment["expected"]))
        print(validate_amount(payment["paid"]))

        outstanding_amnt = payment["expected"] - payment["paid"]
        
        print(outstanding_amnt)

    for payment in payments:
        outstanding_amnt = payment["expected"] - payment["paid"]
        if outstanding_amnt > 0:
            print(payment["baby"])

    for payment in payments:
        if payment["expected"] >= 0:
            print("Good entry")
        else:
            print("invalid")

    

calculate_totals()