# isinstance(object, <datatype>)

## what it does;

This validates whether a value is of a given data type or not


## what you give it;

You give it the value you're checking and the target data type

## what it returns;

I think it returns True or False by default but can also return another custom result you set when the value fits the data type

## one small example written by you.

value = 20
if isinstance(value, int):
    print("Number detected")


# dict.items() in a For loop

## what it does;

I think it returns a new view of a dictionary's items in key, value pairs

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

=+ refers to a new value regardless of what iterated before it while += refers to adding the new value to what it found in place

## what you give it;

I think it depends on one's goal. and I think you give it the original value and the numbers in an array to loop through

## what it returns;

It returns the final value

## one small example written by you.

numbers = [4, 5, 4]
sum = 4

for number in numbers:
    sum=+number ---The sum will be equal to 4 plus the numbers as they loop through the list. So it will be 8, then 9, then 8

    sume+=number ---In the first iteration, the sum will be 8, then 13, then 17 respectively, so it adds on what it has found



