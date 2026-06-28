"""Today is Day 10 of my Learning Python journey. Today I have learnt:-
1. Date Module
2. Built-in Math Functions and Math Module"""

import datetime
import math

today_date_and_time = datetime.datetime.now()
print(today_date_and_time)

# Using strftime() method

print(today_date_and_time.strftime("%Y-%m-%d %H:%M:%S"))

#Math

number_list = [100, 281, 396, 155, 98, 707]
print(max(number_list))
print(min(number_list))

print(abs(-40.7))

power_example = pow(2, 3)
print(power_example)

## Using the math module

number = 101
print(math.sqrt(number))
print(math.ceil(math.sqrt(number)))
print(math.floor(math.sqrt(number)))