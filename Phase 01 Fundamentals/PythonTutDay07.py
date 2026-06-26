"""This is Day 07 of my Python Learning Journey. Today I have learnt:-
1. Functions:-
i. Creating, Calling and Naming a Function
ii. Return Values and Pass statement
iii. Arguments - Positional and Keyword; Parameters
iv. *args and **kwargs; Unpacking Arguments
v. Scope - Local and Global; Global and Nonlocal Keywords; Functions Inside Function; The LEGB Rule
vi. Decorators - Arguments in the Decorated Function; *args and **kwargs, Multiple Decorators & Preserving Function Metadata
vii. Lambda and Using Lambda with built-in functions
viii. Recursion - Base Case & Recursive Case; Recursion with Lists; Fibonacci Sequence; Recursion Depth Limit
viii. Generators - yield keyword; using next() with generators; generator expressions; Generator Methods - send() and close()
"""
import sys
import functools
def my_func(a,b): # Creating a function
    return a + b # Using return to return the sum of arguments a and b

x = 5
y = 10
my_func(x,y) # calling the function

def my_empty_function(): # Using pass statement to build the structure and add the logic later
    pass

#Positional and Keyword Arguments
def my_func1(greetings,fname,lname):
    print(f"{greetings}, {fname} {lname}.")

my_func1("Hello", fname="Harshit", lname="Singh") #Mixing Positional and Keyword Arguments

# Positional-only and Keyword-only Arguments
def my_function(a,b,/,*,c,d):
    return a + b + c + d

result = my_function(5, 15, c=20, d=25) #Combining Positional-only and Keyword-only arguments
print(result)

# *args and *kwargs
def my_function_for_args(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function_for_args("Emil", "Tobias", "Linus")

def my_function_for_kwargs(**kwargs):
    print("Type:", type(kwargs))
    print(f"You are {kwargs['name']}, {kwargs['age']} years old and you live in {kwargs["city"]}.")
    print("All Data:", kwargs)

my_function_for_kwargs(name = "Harshit", age = 19, city = "Patna")

def my_function_for_args_and_kwargs(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function_for_args_and_kwargs("User Info", "Harshit", "Singh", age = 19, city = "Patna")

# Unpacking Arguments
def my_function_for_unpacking_lists(a,b,c):
   return a + b + c

numbers = [1,2,3]
result_numbers = my_function_for_unpacking_lists(*numbers)
print(result_numbers)

def my_function_for_unpacking_dictionaries(fname,lname):
   print("Hello", fname, lname)

person = {"fname": "Harshit", "lname": "Singh"}
my_function_for_unpacking_dictionaries(**person)

#Scope
## Global and Nonlocal Keywords
y1 = "Harshit"

def myfunc_for_global():
   global y1
   y1 = "Tihsrah"
   print("Hello", y1)

myfunc_for_global()
print(y1)

def myfunc1():
  x2 = "Jane"
  def myfunc2():
    nonlocal x2
    x2 = "hello"
  myfunc2()
  return x2

print(myfunc1())


## The LEGB Rule
x1 = "global"
def outer():
    x1 = "enclosing"
    def inner():
        x1 = "local"
        print("Inner:", x1)
    inner()
    print("Outer:", x1)

outer()
print("Global:", x1)

#Decorators
def changecase(n):
   def changecase(func):
      @functools.wraps(func)
      def myinner():
        if n == 1:
            a = func().lower()
        else:
           a = func().upper()
        return a
      return myinner
   return changecase

@changecase(1)
def my_Function1():
   return "Hello Harshit"
print(my_Function1())
print(my_Function1.__name__)

#Lambda
Numbers = [1,2,3,4,5]
doubled = list(map(lambda x:x*2, Numbers))
print(doubled)

odd_Numbers = list(filter(lambda x: x%2 != 0, Numbers))
print(odd_Numbers)

the_big_three = [("Naruto",25), ("Luffy",22), ("Ichigo", 28)]
sorted_the_big_three = sorted(the_big_three, key = lambda x:x[1])
print(sorted_the_big_three)

#Recursion
def sum_list(numbers):
   if len(numbers) == 0:
      return 0
   else:
      return numbers[0] + sum_list(numbers[1:])

my_list = [1,2,3,4,5]
print(sum_list(my_list))

print(f"Default Recursion Limit: {sys.getrecursionlimit()}")

#Generator
def fibonacci():
   a,b = 0,1
   while True:
      yield a
      a, b=b, a+b

##Getting first 100 Fibonacci Numbers
gen = fibonacci()
for _ in range(100):
   print(next(gen))

## Using send() and close() methods
def echo_generator():
   while True:
      received = yield
      print("Received:", received)

gen1 = echo_generator()
next(gen1) # Prime the generator
gen1.send("Hello")
gen1.send("World")

def my_gen():
   try:
      yield 1
      yield 2
      yield 3
   finally:
      print("Generator Closed")

gen2 = my_gen()
print(next(gen2))
gen2.close()