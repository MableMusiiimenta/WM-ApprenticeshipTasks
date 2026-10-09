For each example below:

Do not run it first.
Write what you predict will happen.
Where useful, write the values of the variables step by step.
Then run it.
Record the actual result.
If your prediction was different, explain what you misunderstood.

## Example 1:

numbers = [3, 5, 7]
total = 0

for number in numbers:
    total += number

print(total)

### Write what I predict will happen:

As the loop iterates through the list/array, the total will be increased by the number in iteration.
So the total being 0 at the start, the 1st iteration will make it 3, the 2nd iteration will make it 8 and the 3rd iteration will make it 15.
Therefore result is 15

### Actual Result
15

## Example 2:

numbers = [3, 5, 7]
total = 0

for number in numbers:
    total =+ number

print(total)

### Write what I predict will happen:

I think as the loop iterates through the list/array, the total will become the number in iteration.
So the total being 0 at the start, the 1st iteration will make it 3, the 2nd iteration will make it 5 and the 3rd iteration will make it 7.
Therefore result is 7 since it's the last iterated number

### Actual Result
7

## Example 3:

def check(value):
    if value < 0:
        return "negative"

    if value == 0:
        return "zero"

    return "positive"

# print(check(-4))
### Write what I predict will happen:

I think the result will be "negative" because -4 fits the first if statement and so the program won't run any farther.

### Actual Result
negative


# print(check(0))
### Write what I predict will happen:
this will be "zero" because the program will run the 1st if and proceed to the next if because 0 does not meet the first condition,then it will stop at the second if because it fits 0 since 0 == 0 and so will return "zero"

### Actual Result
zero


# print(check(8))
### Write what I predict will happen:
 
 and this will return "positive" since 8 does not fit any of the two if conditions, so what is left for it is the closing return result which is "positive".

### Actual Result
positive




## Example 4:

age = 17
has_permission = True

if age >= 18 and has_permission:
    print("allowed")
else:
    print("not allowed")
Then change and to or and predict the result again before running it.

# with 'and'
### Write what I predict will happen:

With and, the result will be "not allowed" because it requires for both conditions to be true but only one is met.The person has permission but their age < 18.

### Actual Result
not allowed

# with 'or'
### Write what I predict will happen:
With or, I think the result will be "allowed" because one of the conditions is met and so the program runs smoothly

### Actual Result
allowed

## Example 5:

def double(value):
    result = value * 2
    return result

number = 6
answer = double(number)

print(number)
print(answer)
Explain what number, value, result and answer represent.

### Write what I predict will happen:

I think number represents the argument for the function double, result is product of value(which is number(6)) multiplied by 2 and answer is the variable that stores the result of the double function, and it is 12.

### Actual Result
6
12

## Example 6:

payment = {
    "baby": "Amina",
    "expected": 120000,
    "paid": 80000,
}

for key, value in payment.items():
    print(key, value)
    
Explain what .items() gives the loop and how key differs from value.

### Response:

I think .items() gives the loop the leverage to go through the dictionary since a dictionary is not directly callable. 
Key refers to the label and is placed on the left of an item in the dictionary and value refers to what the label holds/carries and is placed on the right of an item in the dictionary. for example, in "baby":"Amina", baby is the key and Amina is the value

# One additional question: Python treats True in a special way in relation to integers. Use the Python documentation to investigate what:

# isinstance(True, int)
# returns, and write one or two sentences about whether you think True should be accepted as an amount in our application.

It returns True because according to documentation, True is 1 and False is 0. So it is a positive integer number 1.

I think True should not be accepted as an amount because it is not calculatable with other integers.