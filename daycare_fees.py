# Return to your existing daycare_fees.py.

# Please make sure it now:

# validates both expected and paid;
# rejects invalid values before calculations;
# rejects Boolean values;
# calculates total expected;
# calculates total paid;
# calculates total outstanding;
# calculates outstanding per baby;
# lists babies who still have an outstanding balance;
# handles the same baby appearing more than once.
# Please keep the solution simple and readable. I would rather see code you fully understand than a more advanced solution copied from somewhere.


def validate_amount(value):

    if isinstance(value, bool):
         return False
    
    if not isinstance(value, (int, float)):
            return False

    if value < 0:
         return False

    return True

def calculate_totals():
    total_expected = 0
    total_paid = 0
    total_outstanding = 0

    payments = [    {"baby": "Amina", "expected": 120000, "paid": 120000},    {"baby": "Joel", "expected": 120000, "paid": 80000},    {"baby": "Grace", "expected": 150000, "paid": 0},    {"baby": "Amina", "expected": 50000, "paid": 50000},]

    for payment in payments:
        print(payment["baby"])
        print(payment["expected"])
        
        print(payment["paid"])
        print(validate_amount(payment["expected"]))
        print(validate_amount(payment["paid"]))
        total_expected += payment["expected"]
        total_paid += payment["paid"]
        
    
        outstanding_amnt = payment["expected"] - payment["paid"]
        
        print(outstanding_amnt)
        total_outstanding += outstanding_amnt

    for payment in payments:
        outstanding_amnt = payment["expected"] - payment["paid"]
        if outstanding_amnt > 0:
            print(payment["baby"])
        
    print(total_expected)
    print(total_paid)
    print(total_outstanding)
   

calculate_totals()