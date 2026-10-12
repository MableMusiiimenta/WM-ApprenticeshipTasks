
Trace this program line by line before running it:

balance = 100 ---the variable is balance and its value is 100. Its data type is a postive integer
payment = 30  ---the variable is payment and its value is 30. Its an integer type

balance = balance - payment  ---the variable is balance and its value is the difference of balance and payment variables assigned above, which is 70

fee = 10   ---the variable is fee and its value is 10. It is an integer type

balance = balance - fee   ---the variable is balance and its value is the difference of most previous balance and fee, which makes it 60

has_money = balance > 0 ---this is variable balance whose value is a boolean comparing balance to 0. It determines if balance is greater than 0

print(balance)    ---this will print 60 because it is the value assigned to the most previous balance variable
print(has_money)   ---this will print True because balanceis 60 and so is greater than 0

Use a table like:

Step	                                Variable changed	   Old value	New value
Initial assignment	                       balance	             ---	       100
subtracted payment from old balance	       balance	              100	       70
subtracted fee from old balance	           balance	              70	       60
Calculation	balance	                       balance                ---          60


