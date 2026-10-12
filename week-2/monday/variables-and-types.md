
## Example 1

a = 10  --- a is the variable and its value is 10. It is a positive integer data type
b = a   --- b is the variable and its value is a. It is a positive integer data type since it derives its value from the variable above whose value is 10
a = 20  --- a is the variable and its value is 20. It is a positive integer data type

print(a)  ---i think this will print 20 because 20 is the last value assigned to variable a in the program

print(b)  ---i think this will print 10 because it is the first value of a assigned right before b is compiled



## Example 2
value = "25"  ---the variable is value and its value is "25"

print(type(value))  ---i think this will print str because "25" is a string type

value = int(value)  ---the variable is value and its value is "25" mapped into integer data type so its value is 25, a positive integer

print(type(value))  ---i think this will print int because the new value of variable value is an integer, 25
print(value + 5)    ---i think this will print 30 because it is getting the sum of integer 25 and 5 which is 30


## Example 3
x = 5   ---the varible is x and its value is 5. it is an integer
y = 2   ---the varible is y and its value is 2. it is an integer

result = x * y + 3   ---the variable is result and its value is the sum of the product of 5 and 2, plus 3

print(result)  ---this will print 13 because multiplication comes before addition, so its adding 3 to the product of 5 and 2


## Example 4
result = (5 + 2) * 3  ---the variable is result and its value is the product of the sum of 5 and 2 with 3

print(result)  ---this will print 21 because it shall consider the brackets value first which is 7 and multiply it by 3 which equals 21


## Example 5
age = 17   ---the variable is age and its value is 17. It is a positive integer data type
is_adult = age >= 18  ---the variable is is_adult and its value is a boolean comparing age to 18 to determine if age is greater or equal to 18

print(is_adult) ---this will print False because the value of age which is 17 is less than 18


## Example 6
expected = 120  ---the variable is expected and its value is 120. It is a positive integer data type
paid = 80       ---the variable is paid and its value is 80. It is a positive integer data type

outstanding = expected - paid  ---the variable is outstanding and its value is the difference of 120 amd 80. It is a positive integer data type

print(outstanding)  ---i think this will print 40 because 120 - 80 is 40


## Example 7
expected = 100   ---the variable is expected and its value is 100. its data type is integer
paid = 120       ---the variable is paid and its value is 120. its data type is integer

overpaid = paid > expected  ---the variable is overpaid and its value is a boolean comparison between expected and paid determining whether paid is greater than expected

print(overpaid)   ---i think this will print True because paid which is 120 is greater than expected, which is 100


## Example 8
name = "Amina"   ---the variable is name and its value is "Amina". its data type is string
age = 4          ---the variable is age and its value is 4. its data type is integer

description = name + " is " + str(age) + " years old"

print(description) ---i think this will print Amina is 4 years old


## Example 9
price = 100   ---the variable is price and its value is 100. its data type is integer
quantity = 3  ---the variable is quantity and its value is 3. its data type is integer

total = price * quantity  ---the variable is total and its value is the product of price and quantity, 100 and 3

print(total)   ---i think this will print 300, because 100 multiplied by 3 is 300 and it's the value of variable total


## Example 10
stock = 5    ---the variable is stock and its value is 5. its data type is integer
quantity = 3  ---the variable is quantity and its value is 3. its data type is integer

enough_stock = stock >= quantity   ---the variable is enough_stock and its value is a boolean comparing stock and quantity to determine if stock is greater or equal to quantity

print(enough_stock)  ---this will print True because stock, which is 5 is greater than quantity which is 3


