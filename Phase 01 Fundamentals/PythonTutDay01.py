"""Things I Learned Today:-
1. Python Varibales
2. Python Inputs & Outputs
3. Python Comments
4. Python Datatypes (Just what are they and how to set them)"""

#And that's how you add a comment

print("Hello World", end = " ")
print("I'll print this in the same line.")

#Global Variables and 'Global' Keyword
x = "awesome" #Global Variable

def myfunc():
    x = "hilarious" #Local Variable
    print("Python is " + x) #Will use the local one

myfunc()
print ("Python is " + x) #will use the global one

y = "rainy"

def myfunc2():
    global y
    y = "cloudy"
    print("The weather is " + y + " today.")

myfunc2()
print("The weather is " + y + " today.")
#Here both will use "cloudy" as y's value.

#Python Data Types
a = "Hello World" #str
b = 21 #int
c = 21.1 #float
d = 21j #complex
e = ['cricket', 'football', 'hockey'] #list
f = ("cricket", "football", "hockey") #tuple
g = range(21) #Range
h = {"name" : "Harshit", "age" : 19} #Dict
i = {"cricket", "football", "hockey"} #set
j = frozenset({"cricket", "football", "hockey"}) #frozenset
k = True #bool
l = b"Hello" #bytes
m = bytearray(5) #bytearray
n = memoryview(bytes(5)) #memoryview
o = None #NoneType

#type() function
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))
