# isinstance(object, <datatype>)

## what it does;

This validates whether a value is of a given data type or not


## what you give it;

You give it the value you're checking and the target data type

## what it returns;

I think it returns True if the value fits the given data type and returns False if the value does not fit the given data type

## one small example written by you.

value = 20
if isinstance(value, int):
    print("Number detected")



# dict.items() in a For loop

# what happens when you loop directly over a dictionary;
It returns only the keys for each item in the dictionary

## what it .item() does;

I think it gives you a view of both keys and values to be unpacked in the loop accordingly

## what you give it;

You call it at the end of the name of the dictionary while setting a For loop

## what it returns;

It views dictionary items in their key, value pairs and separates the two when called upon to do so

## one small example written by you.

payments2 = {"baby": "Test", "expected": -5000, "paid": 0, "price": 8.67}

    for key, value in payments2.items():
        print(value)



# =+ vs +=
## what it does;

=+ is not an operator, the number after it just has a positive/plus sign
+= is adds to the existing value

## what you give it;

I think you write what you are trying to add on it

## what it returns;

It returns the final value

## one small example written by you.

numbers = [4, 5, 4]
sum = 0

for number in numbers:
    sum=+number ---The sum will be equal to 4 plus the numbers as they loop through the list. So it will be 4, then 5, then 4

    sume+=number ---In the first iteration, the sum will be 8, then 13, then 17 respectively, so it adds on what it has found

## operators

=  ---This assigns a value to a variable
### example
number = 13 This stores 13 in the variable number

==  ---This states that two things are equal to each other
### example
1 == 1  ---this will return True because 1 is equal to 1

!=  ---This states that item on the left is Not equal to item on the right
### example
1 != 1.2 ---this will return True because 1 is not equal to 1.2


>   ---This states that item on the left is greater than item on the right
### example
3 > 1  ---This will return True because 3 is greater than 1

<   ---This states that item on the left is less than item on the right
### example
3 < 1   ---This will return False because 3 is not less than 1

>=  ---This states that item on the left is greater than or equal to item on the right
### example
7 >= 6 This will return True because 7 is greater than 6

<=  ---This states that item on the left is less than or equal to item on the right
### example
8 <= 7  This will return False because 8 is neither less than 7 nor equal to 7

+   ---This determines the sum of values and is also used when printing variables along with strings in a sentence
### example
6 + 2 ---this will return 8 because 6 plus 2 is 8

-   ---This determines the difference(subtraction) of values
### example
8 - 4 ---This will return 4 because 8 minus 4 is 4

*   ---This is used to calculate the product(multiplication) of values
### example
4 * 2  ---This will return 8 because 4 multiplied by 2 is 8


/   ---This is used to calculate the division of values
### example
16 / 8  ---This will return 2 because 16 divided by 8 is 2


type()  ---This is used to determine which datatype a value fits into
### example
print(type("15"))


int()   ---This is used to map/change a value into an integer type
### example
quantity = "15"
actual_qty = int("15")
print(actual_qty)

float()  ---This is used to map/change a value into a float type
### example
metres = 15
metres_in_decimal = float(15)
print(metres_in_decimal)

str()    ---This is used to map/change a value into a string type
### example
ID = 15
actualID = str(15)
print(actualID)


