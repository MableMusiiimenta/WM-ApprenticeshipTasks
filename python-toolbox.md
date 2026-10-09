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



