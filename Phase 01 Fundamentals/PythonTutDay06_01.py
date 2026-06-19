"""Today is Day 06 of Learning Python. Today, I have learnt:-
1. While Loop
2. For Loop"""

# while Loops
i = 1
while i < 6:
  print(i)
  i += 1

## break statement
i1 = 1
while i1 < 6:
  print(i1)
  if i1 == 3:
    break
  i1 += 1

## continue statement
i2 = 0
while i2 < 6:
  i2 += 1
  if i2 == 3:
    continue
  print(i2)

## else statement
i3 = 1
while i3 < 6:
  print(i3)
  i3 += 1
else:
  print("i3 is no longer less than 6")


# for Loops

## looping through a string
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

## break statement
for y in fruits:
  print(y)
  if y == "banana":
    break

## continue statement
for z in fruits:
  if z == "banana":
    continue
  print(z)

## range() function
for a in range(2, 30, 3):
  print(a)

## else in for loop
for x5 in range(6):
  print(x5)
else:
  print("Finally finished!")

## Nested Loops
adj = ["red", "big", "tasty"]

for x1 in adj:
  for y1 in fruits:
    print(x1, y1)

## Pass Statement
for x2 in [0, 1, 2]:
  pass
