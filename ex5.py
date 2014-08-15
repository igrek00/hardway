# -*- coding: utf-8 -*-

name = 'Sergey Pinchuk'
age = 25 # how old i am
height = 184 # santimeters
weight = 61 # kilogramms
eyes = 'Blue' 
hair = 'Brown'
teeth = 'yellow'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d kilogramms heavy." % weight
print "Actually that's not too heavy. At all."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

