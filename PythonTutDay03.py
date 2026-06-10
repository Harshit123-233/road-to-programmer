"""Today was Day 03 of Learning Python from basic. I learned:-
1. Boolean
2. Python Operators:-
i. Arithmetic Operators
ii. Assignment Operators
iii. Ternary Operators
iv. Comparison Operators
v. Logical Operators
vi. Identity Operators
vii. Membership Operators
viii. Bitwise Operators
ix. Operator Precedence"""


#Boolean (Day 03 of Learning Python)

## Will print 'True'
print(bool("Hello"))
x = 101
print(bool(x))

## Will print 'False'
print(bool())
print(bool(()))
print(bool({}))
print(bool([]))
print(bool(""))
print(bool(0))

## Obtaining False using an object that is made from a class using __len__ function
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

## Creating Functions That will return 'True' Value
def myFunction():
    return True

print(myFunction())

## Using isinstance() to return a boolean value
y = 20
print(isinstance(y, int))

# Python Operators

## Arithmetic Operators
print(x+y) #Adds
print(x-y) #Subtracts
print(x*y) #Multiplies
print(x/y) #Divides
print(x%y) #Modulus, returns the remainder
print(x**y) #Exponentiation
print(x//y) #Floor Division

## Assignment Operators

### Few of them
num1 = 100
num1 = num1 + 3
print(num1)

num1 = num1 - 3
print(num1)


### Walrus Operator ":="
numbers = [1,2,3,4,5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements.")

## Ternary Operators
num = 6
x1 = "Weekend!" if num > 5 else "Workday" 
print(f"Today is a {x1}.")

## Comparison Operators

### Few Examples
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print (1 < x < 1000)
print (1 < x and 1 < 1000)

## Logical Operators
print(x > 10 and x > 100)
print(x > 100 or x < 50 )
print(not(x > 100 or x < 50))

## Identity Operators
xList = [1,2,3,4,5]
yList = [1,2,3,4,5]
z = x

print(x is z)
print(x is y)
print(x == y)
print(x is not y)

## Membership Operators:-

### In List
fruits = ['apple', 'banana', 'orange']
print('banana' in fruits)
print('pineapple' not in fruits)

### In Strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# Bitwise Operators
x11 = 2
y11 = 3
print(x11 & y11)
print(x11 | y11)
print(x11 ^ y11)
print(~x11)
print(x11 >> 2)
print(x11 << 2)

## Operator Precedence
print((6 + 3) - (6 + 3))