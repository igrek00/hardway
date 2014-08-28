# -*- coding: utf-8 -*-

def add(a, b):
	print "ADDING %r + %r" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %r - %r" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %r * %r" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %r / %r" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = divide(100, 2)

print "Age: %r, Height: %r, Weight: %r, IQ: %r" % (age, height, weight, iq)

# A puzzle for the extra credit, write it anyway.
print "Here is the puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
new_what = (height - (weight * (iq / 2))) + age

print "That becomes:", what, "Can you do it by hand?"
print "New one is:", new_what, "Is it correct?"

print "New formula is 'a + b/c - d'"
print "Enter new values for a, b, c, d."
a = float(raw_input("a: "))
b = float(raw_input("b: "))
c = float(raw_input("c: "))
d = float(raw_input("d: "))

print "OK, let's check 'a' is %d, 'b' is %d, 'c' is %d, 'd' is %d That's right?" % (a, b, c, d)
print "Now let's do the calculations!"
print "Answer is %d" % subtract(add(a, divide(b, c)), d)
