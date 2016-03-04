"""
File: <sum_powers.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<use while loops to calculate continuously>
"""
user_input = raw_input("Enter a float number: ")
b = float(user_input)
while b == 1.0:
    user_input = raw_input("Enter a float number not equal to 1.0: ")
    b = float(user_input)

user_input = raw_input("Enter a natural number: ")
n = int(user_input)
n = 1
i = 0
while i <= b:
   n += b**i
   i = i +1
print "Total is equal to %d" %n
print (b**(n+1)-1)/(b-1)
