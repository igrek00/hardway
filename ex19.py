# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers): # def function
	print "You have %r cheeses!" % cheese_count # printing
	print "You have %r boxes of crackers!" % boxes_of_crackers # printing
	print "Man, that's enough for party!" # printing
	print "Get a blanket.\n" # printing

print "We can just give the function numbers directly:" # pre-function printing
cheese_and_crackers(20, 30) # function with integers in argument

print "OR, we can use variables from our script:" # variable declaring
amount_of_cheese = 10 # variable declaring
amount_of_crackers = 20 # variable declaring

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # function with variables in argument

print "We can even do math inside too:" # pre-function printing
cheese_and_crackers(10 + 20, 5 + 6) # function with math in argument

print "And we can combine the two, variables and the math" # pre-phase printing to function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # function with complex arugemnt - variable plus integer

