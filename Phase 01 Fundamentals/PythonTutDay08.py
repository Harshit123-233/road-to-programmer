"""Today is Day 08 of my Learning Python Journey. Today, I have learnt:-
1. Range - Creating Ranges; Calling Ranges with one, two or three arguments; Using Ranges; Slicing; Membership Testing; Length of a range
2. Iterators - Iterator vs Iterables, Looping Through an Iterator, Creating an Iterator and StopIteration"""

#Range

## to print the odd numbers starting from 1 to 100

my_range = range(1, 100, 2)
print(my_range)

print(6 in my_range)
print(7 in my_range)

#Iterators

## Using __iter__() and __next__()
my_anime_characters = ("Goku", "Vegeta", "Beerus")
myiter = iter(my_anime_characters)

print(next(myiter))
print(next(myiter))
print(next(myiter))

## Creating an Iterator and using StopIteration to prevent it from executing forever

class MyNumbers: #Create an iterator that returns numbers, starting with 1, and each sequence will increase by one and will stop after 20 iterations:

#Note: I haven't learnt about classes yet but I do have a very basic idea of it. This is solely for an example here.

    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):

        if self.a <= 20:

            x = self.a
            self.a += 1
            return x
        
        else:

            raise StopIteration
    
myclass = MyNumbers()
myiter_second = iter(myclass)

for x in myiter_second:
    print(x)
