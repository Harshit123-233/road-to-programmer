"""Today is Day 11 of my Learning Python journey. Today, I have learnt:-
1. Try...Except:-
i. Exception Handling and Python's Built-in Exceptions
ii. else
iii. finally
iv. Raise an Exception"""

my_path = "D:\\Python Learning Files\\Phase 01 Fundamentals\\PythonTutDay11_files\\file_handling_tut.txt"

try:
  f = open(my_path)
  try:
    f.write("Dhappa")
  except:
    print("Kuchh toh gadbad hai Daya, kuchh toh gadbad hai")
  finally:
    f.close()
except:
  print("Yeh toh gadbad hai re baba")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

my_demand = 10

if my_demand < 150:
  raise Exception("150 rupiya lega!")
